from antlr4.error.ErrorListener import ErrorListener


class QuerySyntaxError(Exception):
    """Error de sintaxis personalizado para mostrar mensajes claros."""


class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise QuerySyntaxError(
            f"Error de sintaxis en línea {line}, columna {column}: {msg}"
        )
