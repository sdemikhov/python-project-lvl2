# -*- coding: utf-8 -*-

"""The cli module parse user entered arguments."""

import argparse


def get_parsed_arguments():
    """Return user entered arguments in explicit form."""
    arguments = make_arguments()

    path_to_file1 = get_path_to_file1(arguments)
    path_to_file2 = get_path_to_file2(arguments)
    return (path_to_file1, path_to_file2)


def make_arguments():
    """Return all user entered arguments in argparse form."""
    parser = argparse.ArgumentParser(description='Generate diff')

    parser.add_argument('first_file', action='store')
    parser.add_argument('second_file', action='store')
    parser.add_argument(
        '-f',
        '--format',
        action='store',
        help='set format of output',
        choices=['plain', 'json'],
        metavar='FORMAT',
    )

    return parser.parse_args()


def get_path_to_file1(arguments):
    """Take arguments in argparse form and return path to first file."""
    return arguments.first_file


def get_path_to_file2(arguments):
    """Take arguments in argparse form and return path to second file."""
    return arguments.second_file
