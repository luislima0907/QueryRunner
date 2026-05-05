import json

from compiler.pipeline import compile_query
from execution.engine import execute_plan


"""
 Método principal  para ejecutar un comando query 
 con sus diferentes opciones posibles
 Este es el que orquesta el resto de pasos del proceso
"""
def run_query(sql, file, format, verbose, optimize, target):

    if verbose:
        print(">> SQL:", sql)
        print(">> File:", file)
        print(">> Optimize:", optimize)
        print(">> Target:", target)

    # 1. Compilar query → Execution Plan (IR)
    plan = compile_query(sql=sql, file=file, optimize=optimize)

    if verbose:
        print("\n>> Execution Plan:")
        print(json.dumps(plan, indent=2))

    # 2. Ejecutar plan
    results = execute_plan(plan)

    # 3. Formatear salida
    output = format_output(results, format)

    # impresión en pantalla del resultado según el formato de salida elegido
    # mismo contenido que quedará en el archivo de salida
    print("Results:\n")
    print(output)

    # 4. Guardar resultado si aplica, es decir si se recibe un target json/csv
    # Si no solo se mostrará en pantalla en formato tabla que es por defecto
    if target:
        save_output(output, target)

"""
 Método para dar un formato de salida
 puede recibir el fomato json/csv, si no se recibe por defecto usa el formato tabla
"""
def format_output(results, format_type):
    if format_type == "json":
        return json.dumps(results, indent=2)

    elif format_type == "csv":
        if not results:
            return ""

        headers = results[0].keys()
        lines = [",".join(headers)]

        for r in results:
            lines.append(",".join(str(r[h]) for h in headers))

        return "\n".join(lines)

    else:  # impresion en formato tabla
        return render_table(results)

"""
    Método para renderizar la salida en un formato de tabla cuyos campos están separados por un |
    
"""
def render_table(results):
    if not results:
        return "No results"

    headers = results[0].keys()
    col_widths = {h: len(h) for h in headers}

    for row in results:
        for h in headers:
            col_widths[h] = max(col_widths[h], len(str(row[h])))

    header_row = " | ".join(h.ljust(col_widths[h]) for h in headers)
    separator = "-+-".join("-" * col_widths[h] for h in headers)

    rows = []
    for row in results:
        rows.append(" | ".join(str(row[h]).ljust(col_widths[h]) for h in headers))

    return "\n".join([header_row, separator] + rows)

"""
 Creación de archivo de salida según el formato elegido  json/csv
"""
def save_output(output, target):
    with open(target, "w") as f:
        f.write(output)