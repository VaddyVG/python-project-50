import argparse
import json
from gendiff.scripts.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    # Позиционные аргументы
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    # Опция для формата вывода
    parser.add_argument(
        "-f", "--format",
        help="set format of output",
        type=str,
        default="plain"
    )
    args = parser.parse_args()

    with open(args.first_file) as file1, open(args.second_file) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    diff = generate_diff(data1, data2, args.format)
    print(diff)


if __name__ == "__main__":
    main()
