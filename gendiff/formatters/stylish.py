from gendiff.diff_tree import ADDED, CHANGED, NESTED, REMOVED, UNCHANGED

INDENT_SIZE = 4
SIGN_SHIFT = 2


def to_str(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    return str(value)


def make_indent(depth, with_sign):
    base = depth * INDENT_SIZE
    if with_sign:
        return " " * (base - SIGN_SHIFT)
    return " " * base


def stringify(value, depth):
    if not isinstance(value, dict):
        return to_str(value)

    lines = []
    for key in sorted(value.keys()):
        val = value[key]
        indent = make_indent(depth + 1, with_sign=False)
        val_str = stringify(val, depth + 1)
        lines.append(f"{indent}{key}: {val_str}")

    closing_indent = make_indent(depth, with_sign=False)
    return "{\n" + "\n".join(lines) + "\n" + closing_indent + "}"


def render_added(node, depth):
    indent = make_indent(depth, with_sign=True)
    value_str = stringify(node["value"], depth)
    return [f"{indent}+ {node['key']}: {value_str}"]


def render_removed(node, depth):
    indent = make_indent(depth, with_sign=True)
    value_str = stringify(node["value"], depth)
    return [f"{indent}- {node['key']}: {value_str}"]


def render_unchanged(node, depth):
    indent = make_indent(depth, with_sign=True)
    value_str = stringify(node["value"], depth)
    return [f"{indent}  {node['key']}: {value_str}"]


def render_changed(node, depth):
    indent = make_indent(depth, with_sign=True)
    old_str = stringify(node["old_value"], depth)
    new_str = stringify(node["new_value"], depth)

    return [
        f"{indent}- {node['key']}: {old_str}",
        f"{indent}+ {node['key']}: {new_str}",
    ]


NODE_RENDERERS = {
    ADDED: render_added,
    REMOVED: render_removed,
    UNCHANGED: render_unchanged,
    CHANGED: render_changed,
}


def format_nodes(nodes, depth):
    lines = []

    for node in nodes:
        node_type = node["type"]

        if node_type == NESTED:
            key = node["key"]
            indent = make_indent(depth, with_sign=False)
            lines.append(f"{indent}{key}: {{")
            children_lines = format_nodes(node["children"], depth + 1)
            lines.extend(children_lines)
            closing_indent = make_indent(depth, with_sign=False)
            lines.append(f"{closing_indent}}}")
        else:
            renderer = NODE_RENDERERS[node_type]
            lines.extend(renderer(node, depth))

    return lines


def format_stylish(diff_tree):
    lines = ["{"]
    lines.extend(format_nodes(diff_tree, depth=1))
    lines.append("}")
    return "\n".join(lines)
