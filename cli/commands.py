import json
import time

from compiler.pipeline import compile_query
from execution.engine import execute_plan, PandasEngine, detect_format
from execution.optimizer import SearchAlgorithmOptimizer
from pathlib import Path
import pandas as pd


def run_query(sql, file, format, verbose, optimize, target, algorithm=None):
    if verbose:
        print(">> SQL:", sql)
        display_file = file if file else _extract_source_from_sql(sql)
        print(">> File:", display_file)
        print(">> Optimize:", optimize)
        print(">> Algorithm:", algorithm or "auto")
        print(">> Target:", target)

    start = time.time()

    plan = compile_query(sql=sql, file=file, optimize=optimize)
    
    # Si se especifica algoritmo, agregarlo al plan
    if algorithm:
        plan["forced_algorithm"] = algorithm.upper()

    if verbose:
        print("\n>> Execution Plan (JSON):")
        print(json.dumps(plan, indent=2, default=str))

    results = execute_plan(plan, verbose=verbose)

    # Mostrar el plan de ejecución despues de ejecutar para que muestre el algoritmo detectado
    print_pipeline(plan)

    elapsed = time.time() - start

    output = format_output(results, format, elapsed)

    print("Results:\n")
    print(output)

    # Mostrar información del algoritmo utilizado después de ejecutar
    algorithm_used = plan.get("search_algorithm", "FULL_SCAN")
    if algorithm_used != "FULL_SCAN":
        print(f"Algorithm used: {algorithm_used}")
        algorithm_info = plan.get("algorithm_info", "")
        if algorithm_info:
            print(f"  -> {algorithm_info}")

    if target:
        if not results:
            print("(No se generó archivo de salida: el resultado está vacío)")
        else:
            save_output(output, target)


def format_output(results, format_type, elapsed=0.0):
    if format_type == "json":
        return json.dumps(results, indent=2, default=str)

    elif format_type == "csv":
        if not results:
            return ""

        headers = results[0].keys()
        lines = [",".join(headers)]

        for r in results:
            lines.append(",".join(str(r[h]) for h in headers))

        return "\n".join(lines)

    else:
        return render_table(results, elapsed)


def render_table(results, elapsed=0.0):
    if not results:
        return "No se encontraron resultados para los criterios buscados"

    headers = results[0].keys()
    col_widths = {h: len(h) for h in headers}

    for row in results:
        for h in headers:
            col_widths[h] = max(col_widths[h], len(str(row[h])))

    header_row = " | ".join(h.ljust(col_widths[h]) for h in headers)
    separator = "-+-".join("-" * col_widths[h] for h in headers)

    rows = []
    total_rows = len(results)
    for row in results:
        rows.append(" | ".join(str(row[h]).ljust(col_widths[h]) for h in headers))
    rows.append(separator)
    rows.append(f"{total_rows} Registros encontrados en ({elapsed:.4f} seg)")
    return "\n".join([header_row, separator] + rows)


def save_output(output, target):
    with open(target, "w") as f:
        f.write(output)


def generate_pipeline_visualization(plan):
    """
    Genera una visualización del pipeline/plan de ejecución
    mostrando las operaciones que se realizarán en orden
    """
    pipeline = []

    # Operación 1: SCAN con detección de algoritmo
    source = plan.get("source", "")
    source_format = plan.get("source_format", "")
    
    # Detectar algoritmo de búsqueda
    algorithm = plan.get("search_algorithm", "FULL_SCAN")
    algorithm_info = plan.get("algorithm_info", "")
    
    scan_msg = f"SCAN: Leer archivo '{source}' ({source_format.upper()})"
    if algorithm != "FULL_SCAN":
        scan_msg += f" [{algorithm}]"
    pipeline.append(scan_msg)
    
    if algorithm_info and algorithm != "FULL_SCAN":
        pipeline.append(f"  -> {algorithm_info}")

    # Operación 2: FILTER (DONDE)
    where = plan.get("where")
    if where:
        comparisons = where.get("comparisons", [])
        logical_ops = where.get("logical_operators", [])

        filter_str = ""
        for i, comp in enumerate(comparisons):
            left = comp.get("left", "")
            op = comp.get("operator", "")
            right = comp.get("right", "")
            filter_str += f"{left} {op} {right}"

            if i < len(logical_ops):
                filter_str += f" {logical_ops[i]} "

        pipeline.append(f"FILTER: Aplicar condición WHERE -> {filter_str}")

    # Operación 3: ORDER BY (ORDENAR)
    order_by = plan.get("order_by")
    if order_by:
        columns = order_by.get("columns", [])
        direction = order_by.get("direction", "ASCENDENTE")
        cols_str = ", ".join(columns)
        pipeline.append(f"ORDER BY: Ordenar por {cols_str} ({direction})")

    # Operación 4: LIMIT (HASTA)
    limit = plan.get("limit")
    if limit:
        pipeline.append(f"LIMIT: Limitar resultados a {limit} registros")

    # Operación 5: PROJECT (EXTRAER)
    columns = plan.get("columns", ["*"])
    if columns != ["*"]:
        cols_str = ", ".join(columns)
        pipeline.append(f"PROJECT: Seleccionar columnas -> {cols_str}")
    else:
        pipeline.append(f"PROJECT: Seleccionar todas las columnas (*)")

    # Optimización
    if algorithm != "FULL_SCAN":
        pipeline.append(f"OPTIMIZED: Usando algoritmo {algorithm}")

    return pipeline


def print_pipeline(plan):
    """
    Imprime el pipeline de ejecución de forma visual
    """
    print("\n" + "="*70)
    print("PLAN DE EJECUCIÓN")
    print("="*70)

    pipeline = generate_pipeline_visualization(plan)

    for i, step in enumerate(pipeline, 1):
        print(f"{i}. {step}")

    print("="*70 + "\n")


def _extract_source_from_sql(sql):
    """
    Extrae el nombre del archivo de la consulta
    Busca el patrón: LEER <archivo>
    """
    tokens = sql.split()
    for i, token in enumerate(tokens):
        if token.upper() == "LEER" and i + 1 < len(tokens):
            source = tokens[i + 1]
            # Remover comillas si las tiene
            if source.startswith("'") and source.endswith("'"):
                source = source[1:-1]
            elif source.startswith('"') and source.endswith('"'):
                source = source[1:-1]
            return source
    return None

