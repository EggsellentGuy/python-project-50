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
