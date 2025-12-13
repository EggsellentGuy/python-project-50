#!/usr/bin/env python3

import argparse

from gendiff.core.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Compares two configuration files "
            "and shows a difference"
        ),
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        help="Set format of output",
        dest="format",
    )
    args = parser.parse_args()

    format_name = args.format or "stylish"
    diff = generate_diff(args.first_file, args.second_file, format_name)
    print(diff)


if __name__ == "__main__":
    main()
