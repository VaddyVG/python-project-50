import json
import yaml


def is_supported_format(file_path):
    """Проверяет, поддерживаем ли формат файла (JSON или YAML)."""
    return file_path.endswith('.json') or file_path.endswith('.yaml') \
        or file_path.endswith('.yml')


def load_json(file_path):
    """Загружает данные из JSON файла."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        return ValueError(f"Error reading JSON file: {e}")


def load_yaml(file_path):
    """Загружает данные из YAML файла."""
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise ValueError(f"Error reading YAML file: {e}")


def load_data(file_path):
    """Загружает данные из файла, проверяя его формат (JSON или YAML)."""
    if not is_supported_format(file_path):
        raise ValueError(f"Unsupported file format: {file_path}")
    if file_path.endswith(".json"):
        return load_json(file_path)
    elif file_path.endswith(".yaml") or file_path.endswith(".yml"):
        return load_yaml(file_path)
