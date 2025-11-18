ADDED = "added"
REMOVED = "removed"
UNCHANGED = "unchanged"
CHANGED = "changed"
NESTED = "nested"


def build_diff(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    nodes = []

    for key in keys:
        in1 = key in data1
        in2 = key in data2

        if in1 and in2:
            value1 = data1[key]
            value2 = data2[key]

            if isinstance(value1, dict) and isinstance(value2, dict):
                nodes.append({
                    "key": key,
                    "type": NESTED,
                    "children": build_diff(value1, value2),
                })
            elif value1 == value2:
                nodes.append({
                    "key": key,
                    "type": UNCHANGED,
                    "value": value1,
                })
            else:
                nodes.append({
                    "key": key,
                    "type": CHANGED,
                    "old_value": value1,
                    "new_value": value2,
                })
        elif in1:
            nodes.append({
                "key": key,
                "type": REMOVED,
                "value": data1[key],
            })
        else:
            nodes.append({
                "key": key,
                "type": ADDED,
                "value": data2[key],
            })

    return nodes
