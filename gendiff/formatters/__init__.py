from gendiff.formatters.stylish import format_stylish


def format_diff(diff_tree, format_name):
    if format_name == "stylish":
        return format_stylish(diff_tree)
    raise ValueError(f"Unknown format: {format_name}")
