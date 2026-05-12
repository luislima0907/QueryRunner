"""
Pipeline completo:
QueryRunner SQL -> Lexer -> Parser -> Árbol sintáctico -> Logical Plan
"""
from antlr4 import InputStream, CommonTokenStream

from QueryRunnerLexer import QueryRunnerLexer
from QueryRunnerParser import QueryRunnerParser
from compiler.query_plan_visitor import QueryPlanVisitor
from compiler.syntax_error_listener import ThrowingErrorListener



def compile_query(sql, file=None, optimize=False):
    """
    Compila una consulta del lenguaje QueryRunner usando ANTLR.
    Retorna un plan lógico que luego ejecuta execution/engine.py.
    """

    input_stream = InputStream(sql)

    lexer = QueryRunnerLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(ThrowingErrorListener())

    token_stream = CommonTokenStream(lexer)

    parser = QueryRunnerParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ThrowingErrorListener())

    tree = parser.consulta()

    visitor = QueryPlanVisitor(file=file, optimize=optimize)
    plan = visitor.visit(tree)

    return plan
