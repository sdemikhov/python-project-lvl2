# -*- coding: utf-8 -*-

"""This module makes string representation of diff tree using plain format."""

from gendiff.gendiff_lib import (
    get_diff_tree_items_sorted,
    get_element_type,
    get_element_value,
    get_value_before,
    get_value_after
)


def stringify_diff_tree_plain(diff_tree, ancestors=[]):
    """
    Create string from inner representation of diff using plain format.

    Keyword arguments:
    diff_tree -- inner representation of diff
    ancestors -- sets the list of ancestors for elements
    """
    result = ''
    for key, element in get_diff_tree_items_sorted(diff_tree):
        if get_element_type(element) == 'container':
            element_as_string = stringify_diff_tree_plain(
                get_element_value(element),
                ancestors + [key],
            )
        elif get_element_type(element) == 'unchanged_element':
            continue
        elif get_element_type(element) == 'edited_element':
            element_as_string = stringify_edited_element(
                key,
                get_element_value(element),
                ancestors,
            )
        elif get_element_type(element) == 'deleted_element':
            element_as_string = stringify_deleted_element(
                key,
                ancestors,
            )
        elif get_element_type(element) == 'added_element':
            element_as_string = stringify_added_element(
                key,
                get_element_value(element),
                ancestors,
            )
        result += element_as_string
    return result


EDITED_ELEMENT_TEMPLATE = (
    "Property '{path_to_root}' was changed. From '{before}' to '{after}'\n"
)


def stringify_edited_element(key, value, ancestors):
    """
    Create string from edited element.

    Keyword arguments:
    key -- key of element in inner representation of diff
    value -- value of element in inner representation of diff
    ancestors -- the list of ancestors for element
    """
    path_to_root = '.'.join(ancestors + [key])
    return EDITED_ELEMENT_TEMPLATE.format(
            path_to_root=path_to_root,
            before=stringify_element_value(get_value_before(value)),
            after=stringify_element_value(get_value_after(value)),
        )


DELETED_ELEMENT_TEMPLATE = "Property '{path_to_root}' was removed\n"


def stringify_deleted_element(key, ancestors):
    """
    Create string from deleted element.

    Keyword arguments:
    key -- key of element in inner representation of diff
    ancestors -- the list of ancestors for element
    """
    path_to_root = '.'.join(ancestors + [key])
    return DELETED_ELEMENT_TEMPLATE.format(path_to_root=path_to_root)


ADDED_ELEMENT_TEMPLATE = (
    "Property '{path_to_root}' was added with value: '{value}'\n"
)


def stringify_added_element(key, value, ancestors):
    """
    Create string from added element.

    Keyword arguments:
    key -- key of element in inner representation of diff
    value -- value of element in inner representation of diff
    ancestors -- the list of ancestors for element
    """
    path_to_root = '.'.join(ancestors + [key])
    return ADDED_ELEMENT_TEMPLATE.format(
        path_to_root=path_to_root,
        value=stringify_element_value(value),
    )


def stringify_element_value(value):
    """
    Create string from element's value.

    Keyword arguments:
    value -- value of element in inner representation of diff
    """
    if any(isinstance(value, _type) for _type in [int, float, str, bool]):
        return str(value)
    else:
        return 'complex value'
