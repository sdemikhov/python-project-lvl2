# -*- coding: utf-8 -*-

"""The diff_tree module provides inner representation of diff."""

TYPE_KEY = 'type'
VALUE_KEY = 'value'
VALUE_BEFORE_KEY = 'before'
VALUE_AFTER_KEY = 'after'

CONTAINER = 'container'
REMOVED = 'deleted_element'
ADDED = 'added_element'
UNCHANGED = 'unchanged_element'
EDITED = 'edited_element'


def make_diff_tree(old_tree, new_tree):
    """
    Create inner representation of diff.

    Arguments:
    old_tree -- content of first loaded file
    new_tree -- content of second loaded file
    """
    diff_tree = {}

    old_tree_keys = old_tree.keys()
    new_tree_keys = new_tree.keys()

    shared_keys = old_tree_keys & new_tree_keys
    old_tree_unique_keys = old_tree_keys - new_tree_keys
    new_tree_unique_keys = new_tree_keys - old_tree_keys

    for old_tree_unique_key in old_tree_unique_keys:
        diff_tree[old_tree_unique_key] = {
            TYPE_KEY: REMOVED,
            VALUE_KEY: old_tree[old_tree_unique_key],
        }

    for new_tree_unique_key in new_tree_unique_keys:
        diff_tree[new_tree_unique_key] = {
            TYPE_KEY: ADDED,
            VALUE_KEY: new_tree[new_tree_unique_key],
        }

    for shared_key in shared_keys:
        old_tree_value_shared = old_tree[shared_key]
        new_tree_value_shared = new_tree[shared_key]
        if old_tree_value_shared == new_tree_value_shared:
            diff_tree[shared_key] = {
                TYPE_KEY: UNCHANGED,
                VALUE_KEY: old_tree_value_shared,
            }
        else:
            if (isinstance(old_tree_value_shared, dict) and 
                    isinstance(new_tree_value_shared, dict)):
                diff_tree[shared_key] = {
                    TYPE_KEY: CONTAINER,
                    VALUE_KEY: make_diff_tree(
                        old_tree_value_shared, new_tree_value_shared
                    ),
                }
            else:
                diff_tree[shared_key] = {
                    TYPE_KEY: EDITED,
                    VALUE_KEY: {
                        VALUE_BEFORE_KEY: old_tree_value_shared,
                        VALUE_AFTER_KEY: new_tree_value_shared,
                    }
                }
    return diff_tree


def get_diff_tree_items_sorted(diff_tree):
    """
    Return the items from inner representation of diff in ascend order.

    Argument:
    diff_tree -- inner representation of diff
    """
    return sorted(diff_tree.items())


def get_element_type(element):
    """
    Return the type of single item in inner representation of diff.

    Keyword arguments:
    element -- single item of diff_tree (inner representation of diff)
    """
    return element[TYPE_KEY]


def get_element_value(element):
    """
    Return the value of single item in inner representation of diff.

    Keyword arguments:
    element -- single item of diff_tree (inner representation of diff)
    """
    return element[VALUE_KEY]


def get_value_before(value):
    """
    Return the 'before' field from value of single edited_element.

    Keyword arguments:
    value -- value field from single item of inner representation of diff
    """
    return value[VALUE_BEFORE_KEY]


def get_value_after(value):
    """
    Return a 'after' field from value of single edited_element.

    Keyword arguments:
    value -- value field from single item of inner representation of diff
    """
    return value[VALUE_AFTER_KEY]
