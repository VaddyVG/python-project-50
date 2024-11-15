def format_value(value):
    """Форматирует значение (переводит булевы значения в строчные)"""
    if isinstance(value, bool):
        return str(value).lower()
    return value


def validate_data(data1, data2):
    """Проверяет, что оба входных данных - это словари."""
    if not isinstance(data1, dict) or not isinstance(data2, dict):
        raise ValueError("Both input data must be dictionaries.")


def format_diff_key(key, value1, value2):
    """Форматирует изменения для конкретного ключа."""
    if value1 != value2:
        return [f"  - {key}: {value1}", f"  + {key}: {value2}"]
    return [f"    {key}: {value1}"]


def generate_diff_for_keys(data1, data2, keys):
    """Генерирует дифф для каждого ключа."""
    diff = []
    for key in keys:
        value1 = format_value(data1.get(key))
        value2 = format_value(data2.get(key))

        if key not in data1:
            diff.append(f"  + {key}: {value2}")
        elif key not in data2:
            diff.append(f"  - {key}: {value1}")
        else:
            diff.extend(format_diff_key(key, value1, value2))
    return diff


def generate_diff(data1, data2, format_type="plain"):
    """Основная функция для генерации диффа между двумя словарями."""
    validate_data(data1, data2)

    # Объединяем все ключи из двух словарей и сортируем
    keys = sorted(data1.keys() | data2.keys())

    # Получаем дифф
    diff = generate_diff_for_keys(data1, data2, keys)

    # Если изменений нет, возращаем пустой словарь
    if not diff:
        return "{}"
    return "{\n" + "\n".join(diff) + "\n}"
