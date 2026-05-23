import hashlib
from pathlib import Path

from src.umgqrunner.gramar.QueryRunnerVisitor import QueryRunnerVisitor


def _fingerprint(query, source):
    raw = f"{query.strip().lower()}|{source or ''}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def _detect_format(source):
    ext = Path(source).suffix.lower().lstrip(".")
    return {"csv": "csv", "json": "json", "tsv": "csv"}.get(ext, "csv")


class QueryPlanVisitor(QueryRunnerVisitor):
    def __init__(self, file=None, optimize=False):
        self.file = file
        self.optimize = optimize
        self._raw_query = ""

    def set_raw_query(self, q):
        self._raw_query = q

    def visitConsulta(self, ctx):
        return self.visit(ctx.declaracionLectura())

    def visitDeclaracionLectura(self, ctx):
        source = self._clean_text(ctx.origen(0).getText())
        source_path = self.file or source
        columns = self.visit(ctx.columnas())

        plan = {
            "fingerprint": _fingerprint(self._raw_query, source_path),
            "op": "Project",
            "columns": columns,
            "source": source_path,
            "source_format": _detect_format(source_path),
            "input": {
                "op": "Scan",
                "source": source_path
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
            plan["limit"] = int(limit_value) if limit_value.isdigit() else limit_value

        if ctx.COMBINAR():
            plan["join"] = {
                "source": self._clean_text(ctx.origen(1).getText()),
                "on": self.visit(ctx.listaIds(-1))
            }

        if self.optimize:
            plan = self._optimize(plan)

        return plan

    def _optimize(self, plan):
        plan["optimized"] = True

        columns = plan.get("columns", ["*"])
        where = plan.get("where")

        if where and columns != ["*"]:
            used_cols = set(columns)
            for comp in where.get("comparisons", []):
                used_cols.add(comp.get("left", ""))
            plan["_usecols"] = list(used_cols)

        return plan

    def visitColumnas(self, ctx):
        if ctx.ASTERISCO():
            return ["*"]
        return self.visit(ctx.listaIds())

    def visitListaIds(self, ctx):
        return [item.getText() for item in ctx.identificador()]

    def visitExpresion(self, ctx):
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

    def visitComparacion(self, ctx):
        values = ctx.valor()
        return {
            "left": self._clean_text(values[0].getText()),
            "operator": ctx.operadorComparacion().getText(),
            "right": self._clean_text(values[1].getText())
        }

    def _clean_text(self, text):
        if (text.startswith('"') and text.endswith('"')) or (text.startswith("'") and text.endswith("'")):
            return text[1:-1]
        return text
