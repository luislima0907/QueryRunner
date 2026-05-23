"""
Módulo de optimizaciones de algoritmos de búsqueda
Determina el mejor algoritmo para ejecutar una consulta
"""

import pandas as pd


class SearchAlgorithmOptimizer:
    """
    Optimiza la elección del algoritmo de búsqueda:
    - SCAN: Lectura completa del archivo
    - INDEX_SCAN: Búsqueda por índice en una columna específica
    - BINARY_SEARCH: Búsqueda binaria si los datos están ordenados
    - HASH_LOOKUP: Búsqueda por hash para igualdades
    """

    @staticmethod
    def can_use_index_scan(plan, df):
        """
        Detecta si se puede usar INDEX_SCAN
        Condiciones:
        - Hay un WHERE clause
        - El WHERE tiene una condición de igualdad (=) en una columna
        - La columna existe en los datos
        """
        where = plan.get("where")
        if not where:
            return False

        comparisons = where.get("comparisons", [])
        logical_ops = where.get("logical_operators", [])

        # INDEX_SCAN solo es útil con UN filtro de igualdad simple
        if len(comparisons) != 1 or len(logical_ops) > 0:
            return False

        comp = comparisons[0]
        operator = comp.get("operator", "")
        left = comp.get("left", "")

        # Solo funciona con igualdad
        if operator != "=":
            return False

        # La columna debe existir
        if left not in df.columns:
            return False

        return True

    @staticmethod
    def can_use_hash_lookup(plan, df):
        """
        Detecta si se puede usar HASH_LOOKUP
        Condiciones: Similar a INDEX_SCAN
        """
        return SearchAlgorithmOptimizer.can_use_index_scan(plan, df)

    @staticmethod
    def can_use_binary_search(plan, df):
        """
        Detecta si se puede usar BINARY_SEARCH
        Condiciones:
        - Hay ORDER BY
        - El WHERE está en la columna del ORDER BY
        - La columna es numérica
        """
        order_by = plan.get("order_by")
        where = plan.get("where")

        if not order_by or not where:
            return False

        order_columns = order_by.get("columns", [])
        comparisons = where.get("comparisons", [])

        if not order_columns or not comparisons:
            return False

        # Verificar que el filtro sea en la misma columna del ORDER BY
        where_column = comparisons[0].get("left", "")

        if where_column not in order_columns:
            return False

        if where_column not in df.columns:
            return False

        # La columna debe ser numérica
        if not pd.api.types.is_numeric_dtype(df[where_column]):
            return False

        return True

    @staticmethod
    def choose_algorithm(plan, df):
        """
        Elige el mejor algoritmo basado en el plan y los datos
        Retorna: (algoritmo, información adicional)
        """
        # Prioridad: BINARY_SEARCH > HASH_LOOKUP > INDEX_SCAN > FULL_SCAN

        if SearchAlgorithmOptimizer.can_use_binary_search(plan, df):
            return ("BINARY_SEARCH", SearchAlgorithmOptimizer._get_binary_search_info(plan))

        if SearchAlgorithmOptimizer.can_use_hash_lookup(plan, df):
            return ("HASH_LOOKUP", SearchAlgorithmOptimizer._get_hash_lookup_info(plan))

        if SearchAlgorithmOptimizer.can_use_index_scan(plan, df):
            return ("INDEX_SCAN", SearchAlgorithmOptimizer._get_index_scan_info(plan))

        return ("FULL_SCAN", "Escaneo completo del archivo")

    @staticmethod
    def _get_index_scan_info(plan):
        """Info para INDEX_SCAN"""
        where = plan.get("where")
        comp = where.get("comparisons", [])[0]
        column = comp.get("left", "")
        value = comp.get("right", "")
        return f"Índice en columna '{column}' buscando valor '{value}'"

    @staticmethod
    def _get_hash_lookup_info(plan):
        """Info para HASH_LOOKUP"""
        where = plan.get("where")
        comp = where.get("comparisons", [])[0]
        column = comp.get("left", "")
        value = comp.get("right", "")
        return f"Hash lookup en columna '{column}' para valor '{value}'"

    @staticmethod
    def _get_binary_search_info(plan):
        """Info para BINARY_SEARCH"""
        where = plan.get("where")
        order_by = plan.get("order_by")

        comp = where.get("comparisons", [])[0]
        column = comp.get("left", "")
        operator = comp.get("operator", "")
        value = comp.get("right", "")

        direction = order_by.get("direction", "ASCENDENTE")

        return f"Búsqueda binaria en '{column}' ({direction}) con condición '{column} {operator} {value}'"

