# Generated from QueryRunner.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .QueryRunnerParser import QueryRunnerParser
else:
    from QueryRunnerParser import QueryRunnerParser

# This class defines a complete listener for a parse tree produced by QueryRunnerParser.
class QueryRunnerListener(ParseTreeListener):

    # Enter a parse tree produced by QueryRunnerParser#consulta.
    def enterConsulta(self, ctx:QueryRunnerParser.ConsultaContext):
        pass

    # Exit a parse tree produced by QueryRunnerParser#consulta.
    def exitConsulta(self, ctx:QueryRunnerParser.ConsultaContext):
        pass


    # Enter a parse tree produced by QueryRunnerParser#declaracionLectura.
    def enterDeclaracionLectura(self, ctx:QueryRunnerParser.DeclaracionLecturaContext):
        pass

    # Exit a parse tree produced by QueryRunnerParser#declaracionLectura.
    def exitDeclaracionLectura(self, ctx:QueryRunnerParser.DeclaracionLecturaContext):
        pass


    # Enter a parse tree produced by QueryRunnerParser#origen.
    def enterOrigen(self, ctx:QueryRunnerParser.OrigenContext):
        pass

    # Exit a parse tree produced by QueryRunnerParser#origen.
    def exitOrigen(self, ctx:QueryRunnerParser.OrigenContext):
        pass


    # Enter a parse tree produced by QueryRunnerParser#columnas.
    def enterColumnas(self, ctx:QueryRunnerParser.ColumnasContext):
        pass

    # Exit a parse tree produced by QueryRunnerParser#columnas.
    def exitColumnas(self, ctx:QueryRunnerParser.ColumnasContext):
        pass


    # Enter a parse tree produced by QueryRunnerParser#listaIds.
    def enterListaIds(self, ctx:QueryRunnerParser.ListaIdsContext):
        pass

    # Exit a parse tree produced by QueryRunnerParser#listaIds.
    def exitListaIds(self, ctx:QueryRunnerParser.ListaIdsContext):
        pass


    # Enter a parse tree produced by QueryRunnerParser#expresion.
    def enterExpresion(self, ctx:QueryRunnerParser.ExpresionContext):
        pass

    # Exit a parse tree produced by QueryRunnerParser#expresion.
    def exitExpresion(self, ctx:QueryRunnerParser.ExpresionContext):
        pass


    # Enter a parse tree produced by QueryRunnerParser#comparacion.
    def enterComparacion(self, ctx:QueryRunnerParser.ComparacionContext):
        pass

    # Exit a parse tree produced by QueryRunnerParser#comparacion.
    def exitComparacion(self, ctx:QueryRunnerParser.ComparacionContext):
        pass


    # Enter a parse tree produced by QueryRunnerParser#operadorComparacion.
    def enterOperadorComparacion(self, ctx:QueryRunnerParser.OperadorComparacionContext):
        pass

    # Exit a parse tree produced by QueryRunnerParser#operadorComparacion.
    def exitOperadorComparacion(self, ctx:QueryRunnerParser.OperadorComparacionContext):
        pass


    # Enter a parse tree produced by QueryRunnerParser#valor.
    def enterValor(self, ctx:QueryRunnerParser.ValorContext):
        pass

    # Exit a parse tree produced by QueryRunnerParser#valor.
    def exitValor(self, ctx:QueryRunnerParser.ValorContext):
        pass


    # Enter a parse tree produced by QueryRunnerParser#orden.
    def enterOrden(self, ctx:QueryRunnerParser.OrdenContext):
        pass

    # Exit a parse tree produced by QueryRunnerParser#orden.
    def exitOrden(self, ctx:QueryRunnerParser.OrdenContext):
        pass


    # Enter a parse tree produced by QueryRunnerParser#identificador.
    def enterIdentificador(self, ctx:QueryRunnerParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by QueryRunnerParser#identificador.
    def exitIdentificador(self, ctx:QueryRunnerParser.IdentificadorContext):
        pass



del QueryRunnerParser