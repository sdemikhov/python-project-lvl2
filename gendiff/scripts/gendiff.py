# -*- coding: utf-8 -*-

"""Run gendiff."""

from gendiff.cli import get_parsed_arguments
from gendiff.gendiff_lib import generate_diff


def main():
    """Entry point for gendiff."""
    diff = generate_diff(*get_parsed_arguments())
    print(diff, end='')


if __name__ == "__main__":
    main()
