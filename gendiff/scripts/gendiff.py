import argparse


def main():
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument("first_file", action="store")
    parser.add_argument("second_file", action="store")
    parser.add_argument(
        "-f",
        "--format",
        action="store",
        help="set format of output",
        choices=["plain", "json"],
        metavar="FORMAT",
    )

    args = parser.parse_args()  # noqa: F841


if __name__ == "__main__":
    main()
