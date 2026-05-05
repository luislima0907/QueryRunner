"""
    Módulo que debe implementar la lógica de construcicón del plan de ejecución de consulta
    basado en la gramática definida y uso de herramienta ANTLR para su transformación
    este plan es entregado al engine quien se ecargará de ejecutar la consulta final al archivo Físico
    y Devolver los resultados
"""

"""
Pipeline completo:
SQL -> AST -> Logical Plan -> Physical Plan -> IR
"""
def compile_query(sql, file, optimize=False):

    # Plan  mock solo para efectos de pruebas y desarrollo
    # Luego debe conectarse toda la lógica usando ANTLR

    plan = {
        "op": "Project",
        "columns": ["*"],
        "input": {
            "op": "Scan",
            "source": file
        }
    }

    if optimize:
        plan["optimized"] = True

    return plan