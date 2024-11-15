import json
import os
from gendiff.scripts.generate_diff import generate_diff


def load_fixture(file_name):
    """Загружает содержимое файла из папки fixtures."""
    path = os.path.join(os.path.dirname(__file__), "fixtures", file_name)
    with open(path, "r") as file:
        return file.read()


def test_generate_diff_plain():
    '''Загрузка данных из фикстур.'''
    data1 = json.loads(load_fixture("data1.json"))
    data2 = json.loads(load_fixture("data2.json"))
    expected_diff = load_fixture("expected_diff_plain.txt").strip()

    # Проверка
    assert generate_diff(data1, data2) == expected_diff


def test_generate_diff_empty_dicts():
    '''Проверка пустых словарей.'''
    data1 = {}
    data2 = {}
    expected_diff = ""
    assert generate_diff(data1, data2) == expected_diff


def test_generate_diff_one_empty_dict():
    '''Проверка для случая, когда один словарь пуст.'''
    data1 = {"key1": "value1"}
    data2 = {}
    expected_diff = "- key1: value1"
    assert generate_diff(data1, data2) == expected_diff
