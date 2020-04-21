# -*- coding: utf-8 -*-

"""The gendiff_lib module provides files comparsion and diff generation."""


def generate_diff(path_to_file1, path_to_file2, output_format='json'):
    """
    Generate string representation of diff.

    Keyword arguments:
    path_to_file1 -- location in a file system for first file
    path_to_file2 -- location in a file system for second file
    output_format --
    """
    data_file1 = load_file(path_to_file1)
    data_file2 = load_file(path_to_file2)

    diff_tree = make_diff_tree(data_file1, data_file2)

    if output_format == 'json':
        diff_tree_as_string = stringify_diff_tree_nested(diff_tree)
    elif output_format == 'plain':
        diff_tree_as_string = stringify_diff_tree_plain(diff_tree)
    return diff_tree_as_string


def make_diff_tree(data_file1, data_file2):
    """
    Create inner representation of diff.

    Keyword arguments:
    data_file1 -- content of first loaded file
    data_file2 -- content of second loaded file
    """
    diff_tree = {}

    keys_file1 = set(data_file1.keys())
    keys_file2 = set(data_file2.keys())

    shared_keys = keys_file1 & keys_file2
    unique_keys_file1 = keys_file1 - keys_file2
    unique_keys_file2 = keys_file2 - keys_file1

    for unique_key1 in unique_keys_file1:
        diff_tree[unique_key1] = {
            'type': 'deleted_element',
            'value': data_file1[unique_key1],
        }

    for unique_key2 in unique_keys_file2:
        diff_tree[unique_key2] = {
            'type': 'added_element',
            'value': data_file2[unique_key2],
        }

    for shared_key in shared_keys:
        if data_file1[shared_key] == data_file2[shared_key]:
            diff_tree[shared_key] = {
                'type': 'unchanged_element',
                'value': data_file1[shared_key],
            }
        else:
            shared_values = (data_file1[shared_key], data_file2[shared_key])
            if all(isinstance(value, dict) for value in shared_values):
                diff_tree[shared_key] = {
                    'type': 'container',
                    'value': make_diff_tree(*shared_values),
                }
            else:
                diff_tree[shared_key] = {
                    'type': 'edited_element',
                    'value': {
                        'before': data_file1[shared_key],
                        'after': data_file2[shared_key],
                    }
                }
    return diff_tree


def get_diff_tree_items_sorted(diff_tree):
    """
    Return the items from inner representation of diff in ascend order.

    Keyword arguments:
    diff_tree -- inner representation of diff
    """
    diff_tree_items = sorted(
        (key, element) for key, element in diff_tree.items()
    )

    for key, element in diff_tree_items:
        yield (key, element)


def get_element_type(element):
    """
    Return the type of single item in inner representation of diff.

    Keyword arguments:
    element -- single item of diff_tree (inner representation of diff)
    """
    return element['type']


def get_element_value(element):
    """
    Return the value of single item in inner representation of diff.

    Keyword arguments:
    element -- single item of diff_tree (inner representation of diff)
    """
    return element['value']


def get_value_before(value):
    """
    Return the 'before' field from value of single edited_element.

    Keyword arguments:
    value -- value field from single item of inner representation of diff
    """
    return value['before']


def get_value_after(value):
    """
    Return a 'after' field from value of single edited_element.

    Keyword arguments:
    value -- value field from single item of inner representation of diff
    """
    return value['after']

# to resolve cyclic import moved to the end of file
from gendiff.file_loader import load_file # noqa E402
from gendiff.nested_stringifier import stringify_diff_tree_nested # noqa E402
from gendiff.plain_stringifier import stringify_diff_tree_plain # noqa E402
