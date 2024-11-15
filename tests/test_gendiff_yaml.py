import pytest
import tempfile
import os
from gendiff.scripts.parse import load_data
from gendiff.scripts.generate_diff import generate_diff


# Фикстура для первого YAML файла
@pytest.fixture
def yaml_file1():
    yaml_data = """
host: hexlet.io
timeout: 50
proxy: 123.234.53.22
follow: false
"""
    # Создаем временный файл для первого yaml
    with tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".yaml") \
            as file:
        file.write(yaml_data)
        file_path = file.name
    yield file_path
    os.remove(file_path)


# Фикстура для второго YAML файла
@pytest.fixture
def yaml_file2():
    yaml_data = """
timeout: 20
verbose: true
host: hexlet.io
"""
    # Создаем временный файл для второго yaml
    with tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".yaml") \
            as file:
        file.write(yaml_data)
        file_path = file.name
    yield file_path
    os.remove(file_path)


# Тест для сравнения двух YAML файлов
def test_generate_diff_yaml(yaml_file1, yaml_file2):
    # Загружаем данные из файлов
    data1 = load_data(yaml_file1)
    data2 = load_data(yaml_file2)

    # Проверяем, что данные загружены корректно
    assert data1 is not None, f"Failed to load data from {yaml_file1}"
    assert data2 is not None, f"Failed to load data from {yaml_file2}"

    # Ожидаемый результат
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    # Проверяем, что функция генерирует правильный вывод
    assert generate_diff(data1, data2, format_type="plain") == expected
