# Generated from QueryRunner.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,32,8,1,1,1,1,1,1,1,1,1,3,1,38,8,1,3,1,40,8,1,1,1,1,1,
        3,1,44,8,1,1,1,1,1,1,1,1,1,1,1,3,1,51,8,1,1,2,1,2,3,2,55,8,2,1,3,
        1,3,3,3,59,8,3,1,4,1,4,1,4,5,4,64,8,4,10,4,12,4,67,9,4,1,5,1,5,1,
        5,5,5,72,8,5,10,5,12,5,75,9,5,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,
        8,3,8,86,8,8,1,9,1,9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,
        18,20,0,3,1,0,9,10,1,0,13,18,1,0,11,12,91,0,22,1,0,0,0,2,25,1,0,
        0,0,4,54,1,0,0,0,6,58,1,0,0,0,8,60,1,0,0,0,10,68,1,0,0,0,12,76,1,
        0,0,0,14,80,1,0,0,0,16,85,1,0,0,0,18,87,1,0,0,0,20,89,1,0,0,0,22,
        23,3,2,1,0,23,24,5,0,0,1,24,1,1,0,0,0,25,26,5,1,0,0,26,27,3,4,2,
        0,27,28,5,2,0,0,28,31,3,6,3,0,29,30,5,3,0,0,30,32,3,10,5,0,31,29,
        1,0,0,0,31,32,1,0,0,0,32,39,1,0,0,0,33,34,5,4,0,0,34,35,5,5,0,0,
        35,37,3,8,4,0,36,38,3,18,9,0,37,36,1,0,0,0,37,38,1,0,0,0,38,40,1,
        0,0,0,39,33,1,0,0,0,39,40,1,0,0,0,40,43,1,0,0,0,41,42,5,6,0,0,42,
        44,3,16,8,0,43,41,1,0,0,0,43,44,1,0,0,0,44,50,1,0,0,0,45,46,5,7,
        0,0,46,47,3,4,2,0,47,48,5,8,0,0,48,49,3,8,4,0,49,51,1,0,0,0,50,45,
        1,0,0,0,50,51,1,0,0,0,51,3,1,0,0,0,52,55,3,20,10,0,53,55,5,21,0,
        0,54,52,1,0,0,0,54,53,1,0,0,0,55,5,1,0,0,0,56,59,5,19,0,0,57,59,
        3,8,4,0,58,56,1,0,0,0,58,57,1,0,0,0,59,7,1,0,0,0,60,65,3,20,10,0,
        61,62,5,20,0,0,62,64,3,20,10,0,63,61,1,0,0,0,64,67,1,0,0,0,65,63,
        1,0,0,0,65,66,1,0,0,0,66,9,1,0,0,0,67,65,1,0,0,0,68,73,3,12,6,0,
        69,70,7,0,0,0,70,72,3,12,6,0,71,69,1,0,0,0,72,75,1,0,0,0,73,71,1,
        0,0,0,73,74,1,0,0,0,74,11,1,0,0,0,75,73,1,0,0,0,76,77,3,16,8,0,77,
        78,3,14,7,0,78,79,3,16,8,0,79,13,1,0,0,0,80,81,7,1,0,0,81,15,1,0,
        0,0,82,86,3,20,10,0,83,86,5,21,0,0,84,86,5,22,0,0,85,82,1,0,0,0,
        85,83,1,0,0,0,85,84,1,0,0,0,86,17,1,0,0,0,87,88,7,2,0,0,88,19,1,
        0,0,0,89,90,5,23,0,0,90,21,1,0,0,0,10,31,37,39,43,50,54,58,65,73,
        85
    ]

class QueryRunnerParser ( Parser ):

    grammarFileName = "QueryRunner.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'LEER'", "'EXTRAER'", "'DONDE'", "'ORDENAR'", 
                     "'POR'", "'HASTA'", "'COMBINAR'", "'EN'", "'Y'", "'O'", 
                     "'ASCENDENTE'", "'DESCENDENTE'", "'>='", "'<='", "<INVALID>", 
                     "'='", "'>'", "'<'", "'*'", "','" ]

    symbolicNames = [ "<INVALID>", "LEER", "EXTRAER", "DONDE", "ORDENAR", 
                      "POR", "HASTA", "COMBINAR", "EN", "Y", "O", "ASCENDENTE", 
                      "DESCENDENTE", "MAYOR_IGUAL", "MENOR_IGUAL", "DIFERENTE", 
                      "IGUAL", "MAYOR", "MENOR", "ASTERISCO", "COMA", "STRING", 
                      "NUMERO", "IDENTIFICADOR", "WS", "COMENTARIO_LINEA", 
                      "COMENTARIO_BLOQUE" ]

    RULE_consulta = 0
    RULE_declaracionLectura = 1
    RULE_origen = 2
    RULE_columnas = 3
    RULE_listaIds = 4
    RULE_expresion = 5
    RULE_comparacion = 6
    RULE_operadorComparacion = 7
    RULE_valor = 8
    RULE_orden = 9
    RULE_identificador = 10

    ruleNames =  [ "consulta", "declaracionLectura", "origen", "columnas", 
                   "listaIds", "expresion", "comparacion", "operadorComparacion", 
                   "valor", "orden", "identificador" ]

    EOF = Token.EOF
    LEER=1
    EXTRAER=2
    DONDE=3
    ORDENAR=4
    POR=5
    HASTA=6
    COMBINAR=7
    EN=8
    Y=9
    O=10
    ASCENDENTE=11
    DESCENDENTE=12
    MAYOR_IGUAL=13
    MENOR_IGUAL=14
    DIFERENTE=15
    IGUAL=16
    MAYOR=17
    MENOR=18
    ASTERISCO=19
    COMA=20
    STRING=21
    NUMERO=22
    IDENTIFICADOR=23
    WS=24
    COMENTARIO_LINEA=25
    COMENTARIO_BLOQUE=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ConsultaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracionLectura(self):
            return self.getTypedRuleContext(QueryRunnerParser.DeclaracionLecturaContext,0)


        def EOF(self):
            return self.getToken(QueryRunnerParser.EOF, 0)

        def getRuleIndex(self):
            return QueryRunnerParser.RULE_consulta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConsulta" ):
                listener.enterConsulta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConsulta" ):
                listener.exitConsulta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConsulta" ):
                return visitor.visitConsulta(self)
            else:
                return visitor.visitChildren(self)




    def consulta(self):

        localctx = QueryRunnerParser.ConsultaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_consulta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.declaracionLectura()
            self.state = 23
            self.match(QueryRunnerParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionLecturaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEER(self):
            return self.getToken(QueryRunnerParser.LEER, 0)

        def origen(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QueryRunnerParser.OrigenContext)
            else:
                return self.getTypedRuleContext(QueryRunnerParser.OrigenContext,i)


        def EXTRAER(self):
            return self.getToken(QueryRunnerParser.EXTRAER, 0)

        def columnas(self):
            return self.getTypedRuleContext(QueryRunnerParser.ColumnasContext,0)


        def DONDE(self):
            return self.getToken(QueryRunnerParser.DONDE, 0)

        def expresion(self):
            return self.getTypedRuleContext(QueryRunnerParser.ExpresionContext,0)


        def ORDENAR(self):
            return self.getToken(QueryRunnerParser.ORDENAR, 0)

        def POR(self):
            return self.getToken(QueryRunnerParser.POR, 0)

        def listaIds(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QueryRunnerParser.ListaIdsContext)
            else:
                return self.getTypedRuleContext(QueryRunnerParser.ListaIdsContext,i)


        def HASTA(self):
            return self.getToken(QueryRunnerParser.HASTA, 0)

        def valor(self):
            return self.getTypedRuleContext(QueryRunnerParser.ValorContext,0)


        def COMBINAR(self):
            return self.getToken(QueryRunnerParser.COMBINAR, 0)

        def EN(self):
            return self.getToken(QueryRunnerParser.EN, 0)

        def orden(self):
            return self.getTypedRuleContext(QueryRunnerParser.OrdenContext,0)


        def getRuleIndex(self):
            return QueryRunnerParser.RULE_declaracionLectura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionLectura" ):
                listener.enterDeclaracionLectura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionLectura" ):
                listener.exitDeclaracionLectura(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionLectura" ):
                return visitor.visitDeclaracionLectura(self)
            else:
                return visitor.visitChildren(self)




    def declaracionLectura(self):

        localctx = QueryRunnerParser.DeclaracionLecturaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracionLectura)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(QueryRunnerParser.LEER)
            self.state = 26
            self.origen()
            self.state = 27
            self.match(QueryRunnerParser.EXTRAER)
            self.state = 28
            self.columnas()
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 29
                self.match(QueryRunnerParser.DONDE)
                self.state = 30
                self.expresion()


            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 33
                self.match(QueryRunnerParser.ORDENAR)
                self.state = 34
                self.match(QueryRunnerParser.POR)
                self.state = 35
                self.listaIds()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11 or _la==12:
                    self.state = 36
                    self.orden()




            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 41
                self.match(QueryRunnerParser.HASTA)
                self.state = 42
                self.valor()


            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 45
                self.match(QueryRunnerParser.COMBINAR)
                self.state = 46
                self.origen()
                self.state = 47
                self.match(QueryRunnerParser.EN)
                self.state = 48
                self.listaIds()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrigenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identificador(self):
            return self.getTypedRuleContext(QueryRunnerParser.IdentificadorContext,0)


        def STRING(self):
            return self.getToken(QueryRunnerParser.STRING, 0)

        def getRuleIndex(self):
            return QueryRunnerParser.RULE_origen

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrigen" ):
                listener.enterOrigen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrigen" ):
                listener.exitOrigen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrigen" ):
                return visitor.visitOrigen(self)
            else:
                return visitor.visitChildren(self)




    def origen(self):

        localctx = QueryRunnerParser.OrigenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_origen)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.identificador()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(QueryRunnerParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASTERISCO(self):
            return self.getToken(QueryRunnerParser.ASTERISCO, 0)

        def listaIds(self):
            return self.getTypedRuleContext(QueryRunnerParser.ListaIdsContext,0)


        def getRuleIndex(self):
            return QueryRunnerParser.RULE_columnas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnas" ):
                listener.enterColumnas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnas" ):
                listener.exitColumnas(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnas" ):
                return visitor.visitColumnas(self)
            else:
                return visitor.visitChildren(self)




    def columnas(self):

        localctx = QueryRunnerParser.ColumnasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_columnas)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(QueryRunnerParser.ASTERISCO)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.listaIds()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaIdsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identificador(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QueryRunnerParser.IdentificadorContext)
            else:
                return self.getTypedRuleContext(QueryRunnerParser.IdentificadorContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(QueryRunnerParser.COMA)
            else:
                return self.getToken(QueryRunnerParser.COMA, i)

        def getRuleIndex(self):
            return QueryRunnerParser.RULE_listaIds

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaIds" ):
                listener.enterListaIds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaIds" ):
                listener.exitListaIds(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaIds" ):
                return visitor.visitListaIds(self)
            else:
                return visitor.visitChildren(self)




    def listaIds(self):

        localctx = QueryRunnerParser.ListaIdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_listaIds)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.identificador()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 61
                self.match(QueryRunnerParser.COMA)
                self.state = 62
                self.identificador()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QueryRunnerParser.ComparacionContext)
            else:
                return self.getTypedRuleContext(QueryRunnerParser.ComparacionContext,i)


        def Y(self, i:int=None):
            if i is None:
                return self.getTokens(QueryRunnerParser.Y)
            else:
                return self.getToken(QueryRunnerParser.Y, i)

        def O(self, i:int=None):
            if i is None:
                return self.getTokens(QueryRunnerParser.O)
            else:
                return self.getToken(QueryRunnerParser.O, i)

        def getRuleIndex(self):
            return QueryRunnerParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)




    def expresion(self):

        localctx = QueryRunnerParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.comparacion()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==10:
                self.state = 69
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 70
                self.comparacion()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QueryRunnerParser.ValorContext)
            else:
                return self.getTypedRuleContext(QueryRunnerParser.ValorContext,i)


        def operadorComparacion(self):
            return self.getTypedRuleContext(QueryRunnerParser.OperadorComparacionContext,0)


        def getRuleIndex(self):
            return QueryRunnerParser.RULE_comparacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacion" ):
                listener.enterComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacion" ):
                listener.exitComparacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparacion" ):
                return visitor.visitComparacion(self)
            else:
                return visitor.visitChildren(self)




    def comparacion(self):

        localctx = QueryRunnerParser.ComparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_comparacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.valor()
            self.state = 77
            self.operadorComparacion()
            self.state = 78
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperadorComparacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IGUAL(self):
            return self.getToken(QueryRunnerParser.IGUAL, 0)

        def DIFERENTE(self):
            return self.getToken(QueryRunnerParser.DIFERENTE, 0)

        def MAYOR_IGUAL(self):
            return self.getToken(QueryRunnerParser.MAYOR_IGUAL, 0)

        def MENOR_IGUAL(self):
            return self.getToken(QueryRunnerParser.MENOR_IGUAL, 0)

        def MAYOR(self):
            return self.getToken(QueryRunnerParser.MAYOR, 0)

        def MENOR(self):
            return self.getToken(QueryRunnerParser.MENOR, 0)

        def getRuleIndex(self):
            return QueryRunnerParser.RULE_operadorComparacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperadorComparacion" ):
                listener.enterOperadorComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperadorComparacion" ):
                listener.exitOperadorComparacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperadorComparacion" ):
                return visitor.visitOperadorComparacion(self)
            else:
                return visitor.visitChildren(self)




    def operadorComparacion(self):

        localctx = QueryRunnerParser.OperadorComparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operadorComparacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identificador(self):
            return self.getTypedRuleContext(QueryRunnerParser.IdentificadorContext,0)


        def STRING(self):
            return self.getToken(QueryRunnerParser.STRING, 0)

        def NUMERO(self):
            return self.getToken(QueryRunnerParser.NUMERO, 0)

        def getRuleIndex(self):
            return QueryRunnerParser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor" ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor" ):
                listener.exitValor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValor" ):
                return visitor.visitValor(self)
            else:
                return visitor.visitChildren(self)




    def valor(self):

        localctx = QueryRunnerParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_valor)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.identificador()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.match(QueryRunnerParser.STRING)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.match(QueryRunnerParser.NUMERO)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrdenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASCENDENTE(self):
            return self.getToken(QueryRunnerParser.ASCENDENTE, 0)

        def DESCENDENTE(self):
            return self.getToken(QueryRunnerParser.DESCENDENTE, 0)

        def getRuleIndex(self):
            return QueryRunnerParser.RULE_orden

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrden" ):
                listener.enterOrden(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrden" ):
                listener.exitOrden(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrden" ):
                return visitor.visitOrden(self)
            else:
                return visitor.visitChildren(self)




    def orden(self):

        localctx = QueryRunnerParser.OrdenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_orden)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentificadorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(QueryRunnerParser.IDENTIFICADOR, 0)

        def getRuleIndex(self):
            return QueryRunnerParser.RULE_identificador

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentificador" ):
                listener.enterIdentificador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentificador" ):
                listener.exitIdentificador(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentificador" ):
                return visitor.visitIdentificador(self)
            else:
                return visitor.visitChildren(self)




    def identificador(self):

        localctx = QueryRunnerParser.IdentificadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_identificador)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(QueryRunnerParser.IDENTIFICADOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





