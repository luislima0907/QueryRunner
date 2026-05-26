from antlr4.error.ErrorListener import ErrorListener


class QuerySyntaxError(Exception):
    """Error de sintaxis personalizado para mostrar mensajes claros."""
    pass


class ThrowingErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol,
                    line, column, msg, e):

        token = offendingSymbol.text if offendingSymbol else "EOF"

        raise QuerySyntaxError(
            f"\n[ERROR SINTÁCTICO]"
            f"\nLínea: {line}"
            f"\nColumna: {column}"
            f"\nToken inesperado: '{token}'"
            f"\nDetalle: {msg}\n"
        )