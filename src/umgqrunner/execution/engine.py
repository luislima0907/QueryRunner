import hashlib
import json
from pathlib import Path

import pandas as pd

from umgqrunner.execution.optimizer import SearchAlgorithmOptimizer


CACHE_DIR = Path.home() / ".queryrunner_cache"


class ColumnValidationError(ValueError):
    pass


class PlanCache:
    @staticmethod
    def _fingerprint(query, source):
        raw = f"{query.strip().lower()}|{source or ''}"
        return hashlib.sha256(raw.encode()).hexdigest()[:16]

    @staticmethod
    def path_for(query, source):
        fp = PlanCache._fingerprint(query, source)
        return CACHE_DIR / f"{fp}.json"

    @staticmethod
    def save(plan, query, source):
        path = PlanCache.path_for(query, source)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(plan, indent=2, default=str))

    @staticmethod
    def load(query, source):
        path = PlanCache.path_for(query, source)
        if path.exists():
            return json.loads(path.read_text())
        return None


def detect_format(source):
    ext = Path(source).suffix.lower().lstrip(".")
    return {"csv": "csv", "json": "json", "tsv": "csv"}.get(ext, "json")


def _convert_value(value):
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value
    return value


class PandasEngine:
    @staticmethod
    def validate_columns(plan):
        source = plan.get("source") or plan.get("input", {}).get("source", "")
        source_format = plan.get("source_format") or detect_format(source)

        actual_columns = PandasEngine._get_schema(source, source_format)
        if actual_columns is None:
            return

        errors = []

        columns = plan.get("columns", ["*"])
        if columns != ["*"]:
            missing = [c for c in columns if c not in actual_columns]
            if missing:
                errors.append(f"Columnas en EXTRAER no existen: {', '.join(missing)}")

        where = plan.get("where")
        if where:
            for comp in where.get("comparisons", []):
                left = comp.get("left", "")
                if left not in actual_columns:
                    errors.append(f"Columna '{left}' usada en filtro DONDE no existe en el archivo")

        order_by = plan.get("order_by")
        if order_by:
            missing_order = [c for c in order_by.get("columns", []) if c not in actual_columns]
            if missing_order:
                errors.append(f"Columnas en ORDENAR POR no existen: {', '.join(missing_order)}")

        if errors:
            raise ColumnValidationError(
                f"El archivo '{source}' tiene estas columnas: {', '.join(actual_columns)}\n"
                + "\n".join(errors)
            )

    @staticmethod
    def _get_schema(source, source_format):
        if not source or not Path(source).exists():
            return None
        try:
            if source_format == "csv":
                return list(pd.read_csv(source, nrows=0).columns)
            elif source_format == "json":
                try:
                    df = pd.read_json(source, nrows=1)
                except ValueError:
                    df = pd.read_json(source, lines=True, nrows=1)
                return list(df.columns)
        except Exception:
            return None
        return None

    @staticmethod
    def execute_plan(plan, verbose=False):
        PandasEngine.validate_columns(plan)

        source = plan.get("source") or plan.get("input", {}).get("source", "")
        source_format = plan.get("source_format") or detect_format(source)
        columns = plan.get("columns", ["*"])

        use_cols = plan.get("_usecols")
        if use_cols is None and columns != ["*"]:
            use_cols = columns

        if verbose:
            print(f">> Loading {source} (format={source_format})")

        where = plan.get("where")
        order_by = plan.get("order_by")
        limit = plan.get("limit")

        can_chunk = source_format == "csv" and _should_chunk(source)

        if can_chunk:
            result = PandasEngine._execute_chunked(source, use_cols, where, order_by, limit, verbose)
        else:
            result = PandasEngine._execute_in_memory(source, source_format, use_cols, where, order_by, limit, verbose, plan)

        if result is None or result.empty:
            return []

        if columns != ["*"]:
            result = result[[c for c in columns if c in result.columns]]

        return result.to_dict(orient="records")

    @staticmethod
    def _execute_in_memory(source, source_format, use_cols, where, order_by, limit, verbose, plan):
        df = PandasEngine._load_data(source, source_format, use_cols)
        if df is None or df.empty:
            return df
        
        # Detectar algoritmo de búsqueda
        # Si se forzó un algoritmo, usarlo; si no, detectar automáticamente
        if plan.get("forced_algorithm"):
            forced_algo = plan.get("forced_algorithm")
            # Obtener info del algoritmo forzado
            if forced_algo == "BINARY_SEARCH":
                algorithm_info = SearchAlgorithmOptimizer._get_binary_search_info(plan)
            elif forced_algo == "HASH_LOOKUP":
                algorithm_info = SearchAlgorithmOptimizer._get_hash_lookup_info(plan)
            elif forced_algo == "INDEX_SCAN":
                algorithm_info = SearchAlgorithmOptimizer._get_index_scan_info(plan)
            else:
                algorithm_info = "Escaneo completo del archivo"
            
            plan["search_algorithm"] = forced_algo
            plan["algorithm_info"] = algorithm_info
        else:
            # Auto-detectar el mejor algoritmo
            algorithm, algorithm_info = SearchAlgorithmOptimizer.choose_algorithm(plan, df)
            plan["search_algorithm"] = algorithm
            plan["algorithm_info"] = algorithm_info
        
        df = PandasEngine._apply_filter(df, where, verbose)
        df = PandasEngine._apply_order(df, order_by)
        df = PandasEngine._apply_limit(df, limit)
        return df

    @staticmethod
    def _execute_chunked(source, use_cols, where, order_by, limit, verbose):
        chunksize = 50000
        chunks = pd.read_csv(source, usecols=use_cols, chunksize=chunksize)

        if order_by or limit:
            accumulated = []
            for chunk in chunks:
                chunk = PandasEngine._apply_filter(chunk, where, verbose)
                accumulated.append(chunk)

            if not accumulated:
                return None

            df = pd.concat(accumulated, ignore_index=True)
            df = PandasEngine._apply_order(df, order_by)
            df = PandasEngine._apply_limit(df, limit)
            return df

        result_chunks = []
        for chunk in chunks:
            chunk = PandasEngine._apply_filter(chunk, where, verbose)
            if not chunk.empty:
                result_chunks.append(chunk)

        if not result_chunks:
            return None
        return pd.concat(result_chunks, ignore_index=True)

    @staticmethod
    def _load_data(source, source_format, use_cols=None):
        if not source or not Path(source).exists():
            return None

        if source_format == "csv":
            return pd.read_csv(source, usecols=use_cols)
        elif source_format == "json":
            try:
                df = pd.read_json(source)
            except ValueError:
                df = pd.read_json(source, lines=True)
            if use_cols is not None:
                df = df[[c for c in use_cols if c in df.columns]]
            return df
        return pd.read_csv(source, usecols=use_cols)

    @staticmethod
    def _apply_filter(df, where, verbose=False):
        if where is None:
            return df

        comparisons = where.get("comparisons", [])
        logical_ops = where.get("logical_operators", [])

        if not comparisons:
            return df

        masks = []
        for comp in comparisons:
            left = comp["left"]
            operator = comp["operator"]
            right = _convert_value(comp["right"])

            if left not in df.columns:
                masks.append(pd.Series([False] * len(df), index=df.index))
                continue

            col = df[left]
            if operator == "=":
                masks.append(col == right)
            elif operator in ("!=", "<>"):
                masks.append(col != right)
            elif operator == ">":
                masks.append(col > right)
            elif operator == "<":
                masks.append(col < right)
            elif operator == ">=":
                masks.append(col >= right)
            elif operator == "<=":
                masks.append(col <= right)
            else:
                masks.append(pd.Series([True] * len(df), index=df.index))

        if not masks:
            return df

        final_mask = masks[0]
        for i, op in enumerate(logical_ops):
            if i + 1 >= len(masks):
                break
            if op == "Y":
                final_mask = final_mask & masks[i + 1]
            elif op == "O":
                final_mask = final_mask | masks[i + 1]

        return df[final_mask]

    @staticmethod
    def _apply_order(df, order_by):
        if order_by is None or df is None or df.empty:
            return df
        cols = order_by.get("columns", [])
        if not cols:
            return df
        valid_cols = [c for c in cols if c in df.columns]
        if not valid_cols:
            return df
        ascending = order_by.get("direction", "ASCENDENTE").upper() != "DESCENDENTE"
        return df.sort_values(by=valid_cols, ascending=ascending)

    @staticmethod
    def _apply_limit(df, limit):
        if limit is not None and df is not None and not df.empty:
            return df.head(limit)
        return df


def _should_chunk(source):
    if not source or not Path(source).exists():
        return False
    try:
        return Path(source).stat().st_size > 50 * 1024 * 1024
    except OSError:
        return False


def execute_plan(plan, verbose=False):
    return PandasEngine.execute_plan(plan, verbose=verbose)


def save_plan_cache(plan, query, source):
    PlanCache.save(plan, query, source)


def load_plan_cache(query, source):
    return PlanCache.load(query, source)
