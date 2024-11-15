import argparse
from gendiff.scripts.generate_diff import generate_diff
from gendiff.scripts.parse import load_data


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

    data1 = load_data(args.first_file)
    data2 = load_data(args.second_file)

    # Генерируем различия
    diff = generate_diff(data1, data2, args.format)
    print(diff)


if __name__ == "__main__":
    main()
