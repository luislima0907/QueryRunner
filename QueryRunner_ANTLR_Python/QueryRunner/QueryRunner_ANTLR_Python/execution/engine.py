def execute_plan(plan):
    data = [
        {"nombre": "Alice", "edad": 34},
        {"nombre": "Bob", "edad": 28},
        {"nombre": "Carlos", "edad": 17},
        {"nombre": "Diana", "edad": 45},
    ]

    if "where" in plan:
        data = apply_where(data, plan["where"])

    if "order_by" in plan:
        col = plan["order_by"]["columns"][0]
        reverse = plan["order_by"]["direction"] == "DESCENDENTE"
        data = sorted(data, key=lambda row: row.get(col), reverse=reverse)

    if "limit" in plan:
        data = data[:plan["limit"]]

    columns = plan.get("columns", ["*"])
    if columns != ["*"]:
        data = [{col: row.get(col) for col in columns} for row in data]

    return data


def apply_where(data, where):
    result = []

    for row in data:
        comparisons = [
            evaluate_comparison(row, comp)
            for comp in where["comparisons"]
        ]

        operators = where["logical_operators"]

        if not operators:
            final_result = comparisons[0]
        else:
            final_result = comparisons[0]
            for i, op in enumerate(operators):
                if op == "Y":
                    final_result = final_result and comparisons[i + 1]
                elif op == "O":
                    final_result = final_result or comparisons[i + 1]

        if final_result:
            result.append(row)

    return result


def evaluate_comparison(row, comp):
    left = comp["left"]
    operator = comp["operator"]
    right = comp["right"]

    left_value = row.get(left)
    right_value = convert_value(right)

    if operator == "=":
        return left_value == right_value
    if operator in ("!=", "<>"):
        return left_value != right_value
    if operator == ">":
        return left_value > right_value
    if operator == "<":
        return left_value < right_value
    if operator == ">=":
        return left_value >= right_value
    if operator == "<=":
        return left_value <= right_value

    return False


def convert_value(value):
    if isinstance(value, str):
        if value.isdigit():
            return int(value)
        try:
            return float(value)
        except ValueError:
            return value
    return value