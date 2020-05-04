# -*- coding: utf-8 -*-

"""Run gendiff."""

from gendiff.cli import parser
from gendiff.generate_diff import generate_diff


def main():
    """Entry point for gendiff."""
    arguments = parser.parse_args()
    diff = generate_diff(
        arguments.first_file,
        arguments.second_file,
        arguments.output_format,
    )
    print(diff)


if __name__ == "__main__":
    main()
