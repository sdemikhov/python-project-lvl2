# -*- coding: utf-8 -*-

"""The gendiff_lib module provides files comparsion and diff generation."""

from gendiff.file_loader import load_file


def generate_diff(path_to_file1, path_to_file2):
    """
    Generate string representation of diff.

    Keyword arguments:
    path_to_file1 -- location in a file system for first file
    path_to_file2 -- location in a file system for second file
    """
    data_file1 = load_file(path_to_file1)
    data_file2 = load_file(path_to_file2)

    difference = make_difference(data_file1, data_file2)

    return stringify_difference(
        difference,
        start_indent_level=0,
        indent_type='  ',
    )


def make_difference(data_file1, data_file2):
    """
    Create inner representation of diff.

    Keyword arguments:
    data_file1 -- content of first loaded file
    data_file2 -- content of second loaded file
    """
    difference = {}

    keys_file1 = set(data_file1.keys())
    keys_file2 = set(data_file2.keys())

    shared_keys = keys_file1 & keys_file2
    unique_keys_file1 = keys_file1 - keys_file2
    unique_keys_file2 = keys_file2 - keys_file1

    for unique_key1 in unique_keys_file1:
        difference[unique_key1] = {
            'type': 'deleted_element',
            'value': data_file1[unique_key1],
        }

    for unique_key2 in unique_keys_file2:
        difference[unique_key2] = {
            'type': 'added_element',
            'value': data_file2[unique_key2],
        }

    for shared_key in shared_keys:
        if data_file1[shared_key] == data_file2[shared_key]:
            difference[shared_key] = {
                'type': 'unchanged_element',
                'value': data_file1[shared_key],
            }
        else:
            shared_values = (data_file1[shared_key], data_file2[shared_key])
            if all(isinstance(value, dict) for value in shared_values):
                difference[shared_key] = {
                    'type': 'container',
                    'value': make_difference(*shared_values),
                }
            else:
                difference[shared_key] = {
                    'type': 'edited_element',
                    'value': {
                        'before': data_file1[shared_key],
                        'after': data_file2[shared_key],
                    }
                }
    return difference


def get_difference_items_sorted(difference):
    """
    Return the items from inner representation of diff in ascend order.

    Keyword arguments:
    difference -- inner representation of diff
    """
    difference_items = sorted(
        (key, element) for key, element in difference.items()
    )

    for key, element in difference_items:
        yield (key, element)


def get_element_type(element):
    """
    Return the type of single item in inner representation of diff.

    Keyword arguments:
    element -- single item of difference (inner representation of diff)
    """
    return element['type']


def get_element_value(element):
    """
    Return the value of single item in inner representation of diff.

    Keyword arguments:
    element -- single item of difference (inner representation of diff)
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


INDENT_STEP = 1


START_DIFFERENCE_TEMPLATE = '{{\n'
END_DIFFERENCE_TEMPLATE = '{indent}}}\n'


def stringify_difference(difference, start_indent_level, indent_type):
    """
    Create string from inner representation of diff.

    Keyword arguments:
    difference -- inner representation of diff
    start_indent_level -- initial position for first column
    indent_type -- sets indent characters
    """
    indent = indent_type * start_indent_level

    result = START_DIFFERENCE_TEMPLATE.format(indent=indent)

    for key, element in get_difference_items_sorted(difference):
        if get_element_type(element) == 'container':
            content_as_string = stringify_difference(
                get_element_value(element),
                start_indent_level + INDENT_STEP,
                indent_type
            )
            element_as_string = stringify_container(
                key,
                content_as_string,
                indent_type * (start_indent_level + INDENT_STEP)
            )
        elif get_element_type(element) == 'unchanged_element':
            element_as_string = stringify_unchanged_element(
                key,
                get_element_value(element),
                indent_type * (start_indent_level + INDENT_STEP)
            )
        elif get_element_type(element) == 'edited_element':
            element_as_string = stringify_edited_element(
                key,
                get_element_value(element),
                indent_type * (start_indent_level + INDENT_STEP)
            )
        elif get_element_type(element) == 'deleted_element':
            element_as_string = stringify_deleted_element(
                key,
                get_element_value(element),
                indent_type * (start_indent_level + INDENT_STEP)
            )
        elif get_element_type(element) == 'added_element':
            element_as_string = stringify_added_element(
                key,
                get_element_value(element),
                indent_type * (start_indent_level + INDENT_STEP)
            )
        result += element_as_string
    result += END_DIFFERENCE_TEMPLATE.format(indent=indent)
    return result


CONTAINER_TEMPLATE = '{indent}  {key}: {value}'


def stringify_container(key, value, indent):
    """
    Create string from container element.

    Keyword arguments:
    key -- key of element in inner representation of diff
    value -- value of element in inner representation of diff
    indent -- indent characters of certain level
    """
    return CONTAINER_TEMPLATE.format(indent=indent, key=key, value=value)


UNCHANGED_ELEMENT_TEMPLATE = '{indent}  {key}: {value}\n'


def stringify_unchanged_element(key, value, indent):
    """
    Create string from unchanged element.

    Keyword arguments:
    key -- key of element in inner representation of diff
    value -- value of element in inner representation of diff
    indent -- indent characters of certain level
    """
    return UNCHANGED_ELEMENT_TEMPLATE.format(
        indent=indent,
        key=key,
        value=value
    )


EDITED_ELEMENT_TEMPLATE = (
    '{indent}+ {key}: {after}\n{indent}- {key}: {before}\n'
)


def stringify_edited_element(key, value, indent):
    """
    Create string from edited element.

    Keyword arguments:
    key -- key of element in inner representation of diff
    value -- value of element in inner representation of diff
    indent -- indent characters of certain level
    """
    return EDITED_ELEMENT_TEMPLATE.format(
            indent=indent,
            key=key,
            before=get_value_before(value),
            after=get_value_after(value),
        )


DELETED_ELEMENT_TEMPLATE = '{indent}- {key}: {value}\n'


def stringify_deleted_element(key, value, indent):
    """
    Create string from deleted element.

    Keyword arguments:
    key -- key of element in inner representation of diff
    value -- value of element in inner representation of diff
    indent -- indent characters of certain level
    """
    return DELETED_ELEMENT_TEMPLATE.format(indent=indent, key=key, value=value)


ADDED_ELEMENT_TEMPLATE = '{indent}+ {key}: {value}\n'


def stringify_added_element(key, value, indent):
    """
    Create string from added element.

    Keyword arguments:
    key -- key of element in inner representation of diff
    value -- value of element in inner representation of diff
    indent -- indent characters of certain level
    """
    return ADDED_ELEMENT_TEMPLATE.format(indent=indent, key=key, value=value)
