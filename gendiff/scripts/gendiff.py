import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    # Позиционные аргументы
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    # Опция для формата вывода
    parser.add_argument(
        "-f", "--format",
        help="set format of output",
        default="stylish"
    )
    args = parser.parse_args()
    print(f"Selected format: {args.format}")


if __name__ == "__main__":
    main()
