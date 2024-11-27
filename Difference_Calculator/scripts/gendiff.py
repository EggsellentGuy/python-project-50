#!/usr/bin/env python3
import argparse as arg


def main():
    parser = arg.ArgumentParser(
        description="Программа сравнивает два файла и показывает разницу.")
    parser.add_argument(
        'first_file', help="Путь к первому файлу"
    )
    parser.add_argument(
        'second_file', help="Путь ко второму файлу"
    )
    args = parser.parse_args()

    print("Первый файл:", args.first_file)
    print("Второй файл:", args.second_file)


if __name__ == "__main__":
    main()
