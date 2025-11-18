from pathlib import Path

from gendiff.generate_diff import generate_diff


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
