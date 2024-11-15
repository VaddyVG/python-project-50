import pytest
from gendiff.scripts.generate_diff import generate_diff


@pytest.fixture
def data1():
    return {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }


@pytest.fixture
def data2():
    return {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }


def test_generate_diff_plain(data1, data2):
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(data1, data2) == expected


def test_generate_diff_empty_data():
    data1 = {}
    data2 = {}
    expected = "{}"
    assert generate_diff(data1, data2) == expected


def test_generate_diff_added_key():
    data1 = {"key1": "value1"}
    data2 = {"key1": "value1", "key2": "value2"}
    expected = """{
    key1: value1
  + key2: value2
}"""
    assert generate_diff(data1, data2) == expected


def test_generate_diff_removed_key():
    data1 = {"key1": "value1", "key2": "value2"}
    data2 = {"key1": "value1"}
    expected = """{
    key1: value1
  - key2: value2
}"""
    assert generate_diff(data1, data2) == expected


def test_generate_diff_changed_value():
    data1 = {"key1": "value1"}
    data2 = {"key1": "value2"}
    expected = """{
  - key1: value1
  + key1: value2
}"""
    assert generate_diff(data1, data2) == expected
