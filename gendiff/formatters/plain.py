from gendiff.diff_tree import ADDED, CHANGED, NESTED, REMOVED, UNCHANGED


def to_plain_value(value):
    if isinstance(value, dict) or isinstance(value, list):
        return "[complex value]"
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def walk(nodes, parent_path=""):
    lines = []

    for node in nodes:
        key = node["key"]
        node_type = node["type"]
        path = f"{parent_path}.{key}" if parent_path else key

        if node_type == NESTED:
            lines.extend(walk(node["children"], path))
        elif node_type == ADDED:
            value_str = to_plain_value(node["value"])
            lines.append(f"Property '{path}' was added with value: {value_str}")
        elif node_type == REMOVED:
            lines.append(f"Property '{path}' was removed")
        elif node_type == CHANGED:
            old_str = to_plain_value(node["old_value"])
            new_str = to_plain_value(node["new_value"])
            lines.append(
                f"Property '{path}' was updated. From {old_str} to {new_str}",
            )
        elif node_type == UNCHANGED:
            continue
        else:
            raise ValueError(f"Unknown node type: {node_type}")

    return lines


def format_plain(diff_tree):
    return "\n".join(walk(diff_tree))
