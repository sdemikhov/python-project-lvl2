import argparse


def make_arguments():    
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

    return parser.parse_args()


def get_path_to_file1(arguments):
    return arguments.first_file


def get_path_to_file2(arguments):
    return arguments.second_file
