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

    def add(key, type_, value):
        diff_tree[key] = {
            TYPE: type_,
            VALUE: value,
        }

    old_tree_keys = old_tree.keys()
    new_tree_keys = new_tree.keys()

    shared_keys = old_tree_keys & new_tree_keys
    old_tree_unique_keys = old_tree_keys - new_tree_keys
    new_tree_unique_keys = new_tree_keys - old_tree_keys

    for old_tree_unique_key in old_tree_unique_keys:
        old_tree_unique_value = old_tree[old_tree_unique_key]
        add(old_tree_unique_key, REMOVED, old_tree_unique_value)

    for new_tree_unique_key in new_tree_unique_keys:
        new_tree_unique_value = new_tree[new_tree_unique_key]
        add(new_tree_unique_key, ADDED, new_tree_unique_value)

    for shared_key in shared_keys:
        old_tree_value_shared = old_tree[shared_key]
        new_tree_value_shared = new_tree[shared_key]
        if old_tree_value_shared == new_tree_value_shared:
            add(shared_key, UNCHANGED, old_tree_value_shared)
        else:
            if (isinstance(old_tree_value_shared, dict) and
                    isinstance(new_tree_value_shared, dict)):
                trees_shared_key_diff_value = make_diff_tree(
                    old_tree_value_shared, new_tree_value_shared
                )
                add(shared_key, CONTAINER, trees_shared_key_diff_value)
            else:
                edited_value = {
                    VALUE_BEFORE: old_tree_value_shared,
                    VALUE_AFTER: new_tree_value_shared,
                }
                add(shared_key, EDITED, edited_value)
    return diff_tree
