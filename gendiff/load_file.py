# -*- coding: utf-8 -*-

"""The file_loader module provides functions for file loading."""


from pathlib import Path
import json
import yaml


JSON_FILENAME_EXTENSIONS = ['.json']
YAML_FILENAME_EXTENSIONS = ['.yaml', '.yml']


def load_file(path_to_file):
    """Return content of a YAML/JSON file as python object.

    Argument:
    path_to_file -- specifies a unique location in a file system
    """
    filename_suffix = Path(path_to_file).suffix

    if filename_suffix in JSON_FILENAME_EXTENSIONS:
        get_data_from_file = json.load
    elif filename_suffix in YAML_FILENAME_EXTENSIONS:
        get_data_from_file = yaml.safe_load
    else:
        raise(ValueError(
            'Unknown filename extension: {}'.format(path_to_file)
        ))
    with open(path_to_file) as f:
        return get_data_from_file(f)
