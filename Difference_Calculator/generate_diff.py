from Difference_Calculator.read_json_file import read_file


def generate_diff(file_path1, file_path2):
    def format_value(value):
        if isinstance(value, bool):
            return str(value).lower()
        return value

    first_data = read_file(file_path1)
    second_data = read_file(file_path2)

    all_keys = sorted(set(first_data.keys()) | set(second_data.keys()))
    result_line = []

    for key in all_keys:
        key_in_first = key in first_data
        key_in_second = key in second_data

        if key_in_first and key_in_second:
            if first_data[key] == second_data[key]:
                result_line.append(
                    f"    {key}: {format_value(first_data[key])}")
            else:
                result_line.append(
                    f"  - {key}: {format_value(first_data[key])}")
                result_line.append(
                    f"  + {key}: {format_value(second_data[key])}")
        elif key_in_first:
            result_line.append(f"  - {key}: {format_value(first_data[key])}")
        elif key_in_second:
            result_line.append(f"  + {key}: {format_value(second_data[key])}")

    diff_str = "{\n" + "\n".join(result_line) + "\n}"
    return diff_str
