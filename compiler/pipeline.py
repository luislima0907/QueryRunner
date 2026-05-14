from antlr4 import InputStream, CommonTokenStream

from gramar.QueryRunnerLexer import QueryRunnerLexer
from compiler.syntax_error_listener import ThrowingErrorListener
from gramar.QueryRunnerParser import QueryRunnerParser
from compiler.query_plan_visitor import QueryPlanVisitor
from execution.engine import PlanCache


def compile_query(sql, file, optimize=False):
    cached = PlanCache.load(sql, file)
    if cached:
        return cached

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
    visitor.set_raw_query(sql)
    plan = visitor.visit(tree)

    PlanCache.save(plan, sql, file)

    return plan
