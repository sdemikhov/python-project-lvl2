# -*- coding: utf-8 -*-

"""The diff_tree module provides inner representation of diff."""

TYPE = 'type'
VALUE = 'value'
VALUE_BEFORE = 'before'
VALUE_AFTER = 'after'

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
            TYPE: REMOVED,
            VALUE: old_tree[old_tree_unique_key],
        }

    for new_tree_unique_key in new_tree_unique_keys:
        diff_tree[new_tree_unique_key] = {
            TYPE: ADDED,
            VALUE: new_tree[new_tree_unique_key],
        }

    for shared_key in shared_keys:
        old_tree_value_shared = old_tree[shared_key]
        new_tree_value_shared = new_tree[shared_key]
        if old_tree_value_shared == new_tree_value_shared:
            diff_tree[shared_key] = {
                TYPE: UNCHANGED,
                VALUE: old_tree_value_shared,
            }
        else:
            if (isinstance(old_tree_value_shared, dict) and
                    isinstance(new_tree_value_shared, dict)):
                diff_tree[shared_key] = {
                    TYPE: CONTAINER,
                    VALUE: make_diff_tree(
                        old_tree_value_shared, new_tree_value_shared
                    ),
                }
            else:
                diff_tree[shared_key] = {
                    TYPE: EDITED,
                    VALUE: {
                        VALUE_BEFORE: old_tree_value_shared,
                        VALUE_AFTER: new_tree_value_shared,
                    }
                }
    return diff_tree
