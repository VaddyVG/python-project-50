def format_value(value):
    """Форматирует значение (переводит булевы значения в строчные)"""
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(data1, data2, format_type="plain"):
    diff = {}

    # Объединяем все ключи из двух словарей
    keys = sorted(data1.keys() | data2.keys())  # Сортируем ключи по алфавиту

    for key in keys:
        value1 = format_value(data1.get(key))
        value2 = format_value(data2.get(key))

        # Если ключ присутствует только в одном файле
        if value1 is None:
            diff[key] = f"+ {key}: {value2}"
        elif value2 is None:
            diff[key] = f"- {key}: {value1}"
        elif value1 != value2:
            diff[key] = f"- {key}: {value1}\n+ {key}: {value2}"
        else:
            diff[key] = f"  {key}: {value1}"

    return "\n".join(diff.values())
