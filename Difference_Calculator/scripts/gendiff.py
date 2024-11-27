#!/usr/bin/env python3
import argparse as arg
from Difference_Calculator.read_json_file import read_file


def main():
    parser = arg.ArgumentParser(
        description="Compares two configuration files and shows a difference"
    )

    parser.add_argument(
        'first_file'
    )

    parser.add_argument(
        'second_file'
    )

    parser.add_argument(
        '-f', '--format', help="Set format of output"
    )

    args = parser.parse_args()

    first_data = read_file(args.first_file)
    second_data = read_file(args.second_file)


if __name__ == "__main__":
    main()
