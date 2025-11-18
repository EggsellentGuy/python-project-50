import json
from pathlib import Path

from gendiff.diff_tree import build_diff
from gendiff.generate_diff import generate_diff
from gendiff.parsers import parse_file


def p(name):
    return Path(__file__).parent / "test_data" / name


def read_text(name):
    return (p(name)).read_text(encoding="utf-8")


def test_flat_json_stylish():
    got = generate_diff(p("file1.json"), p("file2.json"))
    expected = read_text("expected_stylish_flat.txt")
    assert got.rstrip() == expected.rstrip()


def test_flat_yaml_stylish():
    got = generate_diff(p("filepath1.yml"), p("filepath2.yml"))
    expected = read_text("expected_stylish_flat.txt")
    assert got.rstrip() == expected.rstrip()


def test_nested_json_stylish():
    got = generate_diff(p("file1_nested.json"), p("file2_nested.json"))
    expected = read_text("expected_stylish_nested.txt")
    assert got.rstrip() == expected.rstrip()


def test_nested_yaml_stylish():
    got = generate_diff(p("file1_nested.yml"), p("file2_nested.yml"))
    expected = read_text("expected_stylish_nested.txt")
    assert got.rstrip() == expected.rstrip()


def test_nested_json_plain():
    got = generate_diff(p("file1_nested.json"),
                        p("file2_nested.json"), "plain")
    expected = read_text("expected_plain_nested.txt")
    assert got.rstrip() == expected.rstrip()


def test_nested_yaml_plain():
    got = generate_diff(p("file1_nested.yml"), p("file2_nested.yml"), "plain")
    expected = read_text("expected_plain_nested.txt")
    assert got.rstrip() == expected.rstrip()


def test_nested_json_json_format():
    file1 = p("file1_nested.json")
    file2 = p("file2_nested.json")

    got = json.loads(generate_diff(file1, file2, "json"))

    first_data = parse_file(file1)
    second_data = parse_file(file2)
    expected = build_diff(first_data, second_data)

    assert got == expected


def test_nested_yaml_json_format():
    file1 = p("file1_nested.yml")
    file2 = p("file2_nested.yml")

    got = json.loads(generate_diff(file1, file2, "json"))

    first_data = parse_file(file1)
    second_data = parse_file(file2)
    expected = build_diff(first_data, second_data)

    assert got == expected
