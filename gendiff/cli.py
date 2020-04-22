# -*- coding: utf-8 -*-

"""The cli module parse user entered arguments."""

import argparse


def get_parsed_arguments():
    """Return user entered arguments in explicit form."""
    arguments = make_arguments()

    path_to_file1 = get_path_to_file1(arguments)
    path_to_file2 = get_path_to_file2(arguments)
    output_format = get_output_format(arguments)
    return (path_to_file1, path_to_file2, output_format)


def make_arguments():
    """Return all user entered arguments in argparse form."""
    parser = argparse.ArgumentParser(description='Generate diff')

    parser.add_argument(
        'first_file',
        action='store',
        help='location in a file system for first file'
        )
    parser.add_argument(
        'second_file',
        action='store',
        help='location in a file system for second file'
        )
    parser.add_argument(
        '-f',
        '--format',
        action='store',
        help=(
            "Output format: 'nested', 'plain', 'json' (default nested)"
        ),
        choices=['nested', 'plain', 'json'],
        metavar='FORMAT',
        dest='output_format',
        default='nested',
    )

    return parser.parse_args()


def get_path_to_file1(arguments):
    """Return path to first file from argparse arguments."""
    return arguments.first_file


def get_path_to_file2(arguments):
    """Return path to second file from argparse arguments."""
    return arguments.second_file


def get_output_format(arguments):
    """Return output format type from argparse arguments."""
    return arguments.output_format
