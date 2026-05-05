from typing import Optional

import typer

from cli.commands import run_query
from cli.replay import start_repl

app = typer.Typer(
    help="QueryRunner - SQL Engine for CSV/JSON",
    invoke_without_command=True,
    context_settings={"help_option_names": ["-h", "--help"]}
)

"""
 Llamado de aplicación sin comandos
 Se ejecutará y creará la terminal interactiva
 Se agregan los comandos solo para que se muestren en la ayuda aunque no se usen en este flujo
"""
@app.callback(invoke_without_command=True)
def main(ctx: typer.Context,
         file: Optional[str] = typer.Option(
        None,
        "--file", "-f",
        help="Input file (CSV or JSON)"
    ),
    format: str = typer.Option(
        "table",
        "--format", "-o",
        help="Output format: table | json | csv"
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose", "-v",
        help="Enable verbose output (debug info)"
    ),
    optimize: bool = typer.Option(
        True,
        "--optimize",
        help="Enable query optimization"
    ),
    target: Optional[str] = typer.Option(
        None,
        "--target", "-t",
        help="Output file (JSON or HTML report)"
    )):

    if ctx.invoked_subcommand is None:
        start_repl()

"""
 Ejecución de comandos directamente al invocar la aplicación
 usando python main.py COMMAND [ARGUMENTS]
"""
@app.command(help="Query run from SQL")
def query(
    sql: str,
    file: Optional[str] = typer.Option(None, "--file", "-f", help="File from where to run the query"),
    format: str = typer.Option("table", "--format", "-o"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
    optimize: bool = typer.Option(True, "--optimize"),
    target: Optional[str] = typer.Option(None, "--target")):

    run_query(sql, file, format, verbose, optimize, target)

if __name__ == '__main__':
    app()
