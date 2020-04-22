# -*- coding: utf-8 -*-

"""This module makes string representation of diff tree using json format."""

from collections import defaultdict
import json

from gendiff.gendiff_lib import (
    get_diff_tree_items_sorted,
    get_element_type,
    get_element_value,
    get_value_before,
    get_value_after
)


def stringify_diff_tree_json(diff_tree):
    """
    Create string from diff tree using json compatible format.

    Keyword arguments:
    diff_tree -- inner representation of diff
    """
    return json.dumps(
        make_json_compatible_tree(diff_tree),
        sort_keys=True,
        indent=2
    )


def make_json_compatible_tree(diff_tree):
    """
    Create json compatible tree from inner representation of diff.

    Keyword arguments:
    diff_tree -- inner representation of diff
    """
    result = defaultdict(dict)

    for key, element in get_diff_tree_items_sorted(diff_tree):
        if get_element_type(element) == 'container':
            result[key] = make_json_compatible_tree(get_element_value(element))
        elif get_element_type(element) == 'unchanged_element':
            result[key] = get_element_value(element)
        elif get_element_type(element) == 'edited_element':
            value_before = get_value_before(get_element_value(element))
            value_after = get_value_after(get_element_value(element))
            result['__edited__'][key] = {
                '__before__': value_before,
                '__after__': value_after,
            }
        elif get_element_type(element) == 'deleted_element':
            result['__deleted__'][key] = get_element_value(element)
        elif get_element_type(element) == 'added_element':
            result['__added__'][key] = get_element_value(element)
    return result
