import pytest
from gendiff.scripts.generate_diff import validate_data
from gendiff.scripts.generate_diff import format_diff_key
from gendiff.scripts.generate_diff import generate_diff_for_keys
from gendiff.scripts.parse import (is_supported_format, load_data)


def test_validate_data():
    with pytest.raises(ValueError):
        validate_data(None, {})

    with pytest.raises(ValueError):
        validate_data({}, None)

    # Если оба параметра - словари, ошибок не будет
    validate_data({}, {})


def test_format_diff_key():
    assert format_diff_key("key", "old_value", "new_value") == [
        "  - key: old_value",
        "  + key: new_value"
    ]

    assert format_diff_key("key", "same_value", "same_value") == [
        "    key: same_value"
    ]


def test_generate_diff_for_keys():
    data1 = {"key1": "value1", "key2": "value2"}
    data2 = {"key1": "value1", "key2": "value3"}
    keys = ["key1", "key2"]

    diff = generate_diff_for_keys(data1, data2, keys)
    assert diff == [
        "    key1: value1",
        "  - key2: value2",
        "  + key2: value3"
    ]


def test_is_supported_format():
    assert is_supported_format('file.json')
    assert is_supported_format('file.yaml')
    assert is_supported_format('file.yml')
    assert not is_supported_format('file.txt')


def test_load_json():
    # Мокировать загрузку JSON, чтобы избежать ошибок в тестах
    # Пример: mock json.load для теста, чтобы проверить правильность обработки
    pass


def test_load_yaml():
    # Мокировать загрузку YAML, чтобы избежать ошибок в тестах
    pass


def test_load_data():
    with pytest.raises(ValueError):
        load_data('file.txt')  # Не поддерживаемый формат
