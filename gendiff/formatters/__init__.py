from gendiff.formatters.json_ import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def format_diff(diff_tree, format_name):
    if format_name == "stylish":
        return format_stylish(diff_tree)
    if format_name == "plain":
        return format_plain(diff_tree)
    if format_name == "json":
        return format_json(diff_tree)
    raise ValueError(f"Unknown format: {format_name}")
