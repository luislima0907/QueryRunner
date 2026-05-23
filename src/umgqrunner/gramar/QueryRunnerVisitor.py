# Generated from QueryRunner.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .QueryRunnerParser import QueryRunnerParser
else:
    from QueryRunnerParser import QueryRunnerParser

# This class defines a complete generic visitor for a parse tree produced by QueryRunnerParser.

class QueryRunnerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by QueryRunnerParser#consulta.
    def visitConsulta(self, ctx:QueryRunnerParser.ConsultaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryRunnerParser#declaracionLectura.
    def visitDeclaracionLectura(self, ctx:QueryRunnerParser.DeclaracionLecturaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryRunnerParser#origen.
    def visitOrigen(self, ctx:QueryRunnerParser.OrigenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryRunnerParser#columnas.
    def visitColumnas(self, ctx:QueryRunnerParser.ColumnasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryRunnerParser#listaIds.
    def visitListaIds(self, ctx:QueryRunnerParser.ListaIdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryRunnerParser#expresion.
    def visitExpresion(self, ctx:QueryRunnerParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryRunnerParser#comparacion.
    def visitComparacion(self, ctx:QueryRunnerParser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryRunnerParser#operadorComparacion.
    def visitOperadorComparacion(self, ctx:QueryRunnerParser.OperadorComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryRunnerParser#valor.
    def visitValor(self, ctx:QueryRunnerParser.ValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryRunnerParser#orden.
    def visitOrden(self, ctx:QueryRunnerParser.OrdenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryRunnerParser#identificador.
    def visitIdentificador(self, ctx:QueryRunnerParser.IdentificadorContext):
        return self.visitChildren(ctx)



del QueryRunnerParser