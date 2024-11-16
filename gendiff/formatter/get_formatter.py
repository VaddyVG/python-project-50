from gendiff.formatter.stylish import format_in_stylish
from gendiff.formatter.plain import format_in_plain
from gendiff.formatter.json import format_is_json


def get_formatter(format_name: str):
    formatters = {
        "stylish": format_in_stylish,
        "plain": format_in_plain,
        "json": format_is_json,
    }
    return formatters.get(format_name)
