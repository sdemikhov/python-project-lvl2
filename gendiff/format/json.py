# -*- coding: utf-8 -*-

"""This module makes string representation of diff tree using json format."""

import json


def format(diff_tree):
    """
    Create string from diff tree using json compatible format.

    Argument:
    diff_tree -- inner representation of diff
    """
    return json.dumps(
        diff_tree,
        sort_keys=True,
        indent=2
    )
