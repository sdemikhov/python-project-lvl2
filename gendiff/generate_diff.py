# -*- coding: utf-8 -*-

"""The gendiff_lib module provides diff generation."""

from gendiff.load_file import load_file
from gendiff import format
from gendiff import diff_tree


def generate_diff(path_to_file1, path_to_file2, output_format=format.DEFAULT):
    """
    Generate string representation of diff.

    Arguments:
    path_to_file1 -- location in a file system for first file
    path_to_file2 -- location in a file system for second file

    Keyword argument:
    output_format -- format type to display diff
    """
    data_file1 = load_file(path_to_file1)
    data_file2 = load_file(path_to_file2)

    tree = diff_tree.make_diff_tree(data_file1, data_file2)

    if output_format == format.DEFAULT:
        diff_tree_as_string = format.default(tree)
    elif output_format == format.PLAIN:
        diff_tree_as_string = format.plain(tree)
    elif output_format == format.JSON:
        diff_tree_as_string = format.json(tree)
    else:
        raise ValueError('Wrong value of output_format')
    return diff_tree_as_string
