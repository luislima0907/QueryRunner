from QueryRunnerVisitor import QueryRunnerVisitor
from QueryRunnerParser import QueryRunnerParser


class QueryPlanVisitor(QueryRunnerVisitor):
    """
    Convierte el árbol sintáctico de ANTLR en un plan lógico simple.
    Este plan luego se entrega al engine para ejecutarlo.
    """

    def __init__(self, file=None, optimize=False):
        self.file = file
        self.optimize = optimize

    def visitConsulta(self, ctx: QueryRunnerParser.ConsultaContext):
        return self.visit(ctx.declaracionLectura())

    def visitDeclaracionLectura(self, ctx: QueryRunnerParser.DeclaracionLecturaContext):

        source = self._clean_text(ctx.origen(0).getText())
        columns = self.visit(ctx.columnas())

        # Validaciones básicas
        if not source:
            raise Exception("Debe indicar una tabla.")

        if not columns:
            raise Exception("Debe indicar columnas.")

        plan = {
            "op": "Project",
            "columns": columns,
            "input": {
                "op": "Scan",
                "source": self.file or source
            }
        }

        if ctx.expresion():
            plan["where"] = self.visit(ctx.expresion())

        if ctx.ORDENAR():
            order_columns = self.visit(ctx.listaIds(0))
            order_type = "ASCENDENTE"

            if ctx.orden():
                order_type = ctx.orden().getText().upper()

            plan["order_by"] = {
                "columns": order_columns,
                "direction": order_type
            }

        if ctx.HASTA():

            limit_value = ctx.valor().getText()

            if limit_value.isdigit():

                limit_value = int(limit_value)

                if limit_value <= 0:
                    raise Exception("HASTA debe ser mayor que 0.")

            plan["limit"] = limit_value

        if ctx.COMBINAR():
            plan["join"] = {
                "source": self._clean_text(ctx.origen(1).getText()),
                "on": self.visit(ctx.listaIds(-1))
            }

        if self.optimize:
            plan["optimized"] = True

        return plan

    def visitColumnas(self, ctx: QueryRunnerParser.ColumnasContext):
        if ctx.ASTERISCO():
            return ["*"]
        return self.visit(ctx.listaIds())

    def visitListaIds(self, ctx: QueryRunnerParser.ListaIdsContext):
        return [item.getText() for item in ctx.identificador()]

    def visitExpresion(self, ctx: QueryRunnerParser.ExpresionContext):
        comparisons = [self.visit(c) for c in ctx.comparacion()]
        operators = []

        for child in ctx.children:
            text = child.getText().upper()

            if text in ("Y", "O"):
                operators.append(text)

        return {
            "comparisons": comparisons,
            "logical_operators": operators
        }

    def visitComparacion(self, ctx: QueryRunnerParser.ComparacionContext):
        values = ctx.valor()

        return {
            "left": self._clean_text(values[0].getText()),
            "operator": ctx.operadorComparacion().getText(),
            "right": self._clean_text(values[1].getText())
        }

    def _clean_text(self, text):

        if (
            (text.startswith('"') and text.endswith('"'))
            or
            (text.startswith("'") and text.endswith("'"))
        ):
            return text[1:-1]

        return text