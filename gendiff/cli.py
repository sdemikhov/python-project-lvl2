# -*- coding: utf-8 -*-

"""The cli module parse user entered arguments."""

import argparse


parser = argparse.ArgumentParser(description='Generate diff')

parser.add_argument(
    'first_file',
    help='location in a file system for first file'
    )
parser.add_argument(
    'second_file',
    help='location in a file system for second file'
    )
parser.add_argument(
    '-f',
    '--format',
    help=(
        "Output format: 'nested', 'plain', 'json' (default nested)"
    ),
    choices=['nested', 'plain', 'json'],
    metavar='FORMAT',
    dest='output_format',
    default='nested',
)
