import json
import time

from compiler.pipeline import compile_query
from execution.engine import execute_plan


def run_query(sql, file, format, verbose, optimize, target):
    if verbose:
        print(">> SQL:", sql)
        print(">> File:", file)
        print(">> Optimize:", optimize)
        print(">> Target:", target)

    start = time.time()

    plan = compile_query(sql=sql, file=file, optimize=optimize)

    if verbose:
        print("\n>> Execution Plan:")
        print(json.dumps(plan, indent=2, default=str))

    results = execute_plan(plan, verbose=verbose)

    elapsed = time.time() - start

    output = format_output(results, format, elapsed)

    print("Results:\n")
    print(output)

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
