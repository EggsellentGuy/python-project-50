from gendiff.core.diff_tree import build_diff
from gendiff.core.parsers import parse_file
from gendiff.formatters import format_diff


def generate_diff(file_path1, file_path2, format_name="stylish"):
    first_data = parse_file(file_path1)
    second_data = parse_file(file_path2)

    diff_tree = build_diff(first_data, second_data)
    return format_diff(diff_tree, format_name)
