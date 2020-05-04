# -*- coding: utf-8 -*-

"""This module makes string representation of diff tree using nested format."""

from gendiff import diff_tree as diff


INDENT = '  '

START_DIFF_TREE = '{'
END_DIFF_TREE = '}'

UNCHANGED_TEMPLATE = '  {key}: {value}'
REMOVED_TEMPLATE = '- {key}: {value}'
ADDED_TEMPLATE = '+ {key}: {value}'


def format(diff_tree):
    """
    Create string from inner representation of diff using nested format.

    Argument:
    diff_tree -- inner representation of diff
    """
    result = [START_DIFF_TREE]

    for key, element in sorted(diff_tree.items()):
        type_ = element[diff.TYPE]
        element_value = element[diff.VALUE]
        if type_ == diff.CONTAINER:
            open_bracket, *other_fields = format(element_value).split('\n')
            result.append(
                UNCHANGED_TEMPLATE.format(
                    key=key,
                    value=open_bracket,
                )
            )
            result.extend([
                INDENT + line for line in other_fields
            ])
        elif type_ == diff.UNCHANGED:
            result.append(
                INDENT + UNCHANGED_TEMPLATE.format(
                    key=key,
                    value=element_value,
                )
            )
        elif type_ == diff.EDITED:
            result.append(
                INDENT + ADDED_TEMPLATE.format(
                    key=key,
                    value=element_value[diff.VALUE_AFTER],
                )
            )
            result.append(
                INDENT + REMOVED_TEMPLATE.format(
                    key=key,
                    value=element_value[diff.VALUE_BEFORE],
                )
            )
        elif type_ == diff.REMOVED:
            result.append(
                INDENT + REMOVED_TEMPLATE.format(
                    key=key,
                    value=element_value,
                )
            )
        elif type_ == diff.ADDED:
            result.append(
                INDENT + ADDED_TEMPLATE.format(
                    key=key,
                    value=element_value,
                )
            )
    result.append(END_DIFF_TREE)
    return '\n'.join(result)
