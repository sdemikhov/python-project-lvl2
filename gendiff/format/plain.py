# -*- coding: utf-8 -*-

"""This module makes string representation of diff tree using plain format."""

from gendiff import diff_tree as diff


PROPERTY_TEMPLATE = "Property '{}' "
REMOVED = "was removed"
EDITED_TEMPLATE = (
    "was changed. From '{before}' to '{after}'"
)
ADDED_TEMPLATE = (
    "was added with value: '{}'"
)


def format(diff_tree):
    """
    Create string from inner representation of diff using plain format.

    Argument:
    diff_tree -- inner representation of diff
    """
    changes = make_changes_list(diff_tree)
    result = [
        PROPERTY_TEMPLATE.format('.'.join(path)) + description
        for path, description in changes
    ]
    return '\n'.join(result)


def make_changes_list(diff_tree):
    """
    Prepare diff to string convertion.

    Argument:
    diff_tree -- inner representation of diff
    """
    result = []
    for key, element in sorted(diff_tree.items()):
        type_ = element[diff.TYPE]
        element_value = element[diff.VALUE]
        if type_ == diff.CONTAINER:
            container_value = [
                ((key, *path), description)
                for path, description in make_changes_list(element_value)
            ]
            result.extend(container_value)
        elif type_ == diff.UNCHANGED:
            continue
        elif type_ == diff.EDITED:
            result.append(((key,), EDITED_TEMPLATE.format(
                before=format_value(element_value[diff.VALUE_BEFORE]),
                after=format_value(element_value[diff.VALUE_AFTER]),
            )))
        elif type_ == diff.REMOVED:
            result.append(((key,), REMOVED))
        elif type_ == diff.ADDED:
            result.append(((key,), ADDED_TEMPLATE.format(
                format_value(element_value)
            )))
    return result


def format_value(value):
    """
    Create string from element's value.

    Argument:
    value -- value of element in inner representation of diff
    """
    if any(isinstance(value, _type) for _type in [int, float, str, bool]):
        return str(value)
    else:
        return 'complex value'
