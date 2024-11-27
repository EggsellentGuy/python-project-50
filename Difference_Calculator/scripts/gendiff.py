#!/usr/bin/env python3
import argparse as arg


def main():
    parser = arg.ArgumentParser(
        description="Compares two configuration files and shows a difference"
    )

    parser.add_argument(
        'first_file', help="The path to the first file"
    )

    parser.add_argument(
        'second_file', help="The path to the second file"
    )

    parser.add_argument(
        '-f', '--format', help="Set format of output"
    )

    args = parser.parse_args()


if __name__ == "__main__":
    main()
