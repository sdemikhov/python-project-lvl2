# -*- coding: utf-8 -*-

"""This module makes string representation of diff tree using nested format."""

from gendiff.diff_tree import (
    get_diff_tree_items_sorted,
    get_element_type,
    get_element_value,
    get_value_before,
    get_value_after
)


INDENT_STEP = 1

START_DIFF_TREE_TEMPLATE = '{{\n'
END_DIFF_TREE_TEMPLATE = '{indent}}}\n'


def format(diff_tree, start_indent_level=0, indent_type='  '):
    """
    Create string from inner representation of diff using nested format.

    Keyword arguments:
    diff_tree -- inner representation of diff
    start_indent_level -- initial position for first column
    indent_type -- sets indent characters
    """
    indent = indent_type * start_indent_level

    result = START_DIFF_TREE_TEMPLATE.format(indent=indent)

    for key, element in get_diff_tree_items_sorted(diff_tree):
        if get_element_type(element) == 'container':
            content_as_string = format(
                get_element_value(element),
                start_indent_level + INDENT_STEP,
                indent_type,
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
    result += END_DIFF_TREE_TEMPLATE.format(indent=indent)
    return result


CONTAINER_TEMPLATE = '{indent}{key}: {value}'


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
