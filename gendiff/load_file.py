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
        data_from_file = get_data_from_json(path_to_file)
    elif filename_suffix in YAML_FILENAME_EXTENSIONS:
        data_from_file = get_data_from_yaml(path_to_file)
    else:
        raise(ValueError(
            'Unknown filename extension: {}'.format(path_to_file)
        ))
    return data_from_file    


def get_data_from_json(path_to_file):
    """Load json file and return content as python object.

    Argument:
    path_to_file -- specifies a unique location in a file system
    """
    with open(path_to_file) as json_file:
        return json.load(json_file)


def get_data_from_yaml(path_to_file):
    """Load json file and return content as python object.

    Argument:
    path_to_file -- specifies a unique location in a file system
    """
    with open(path_to_file) as yaml_file:
        return yaml.safe_load(yaml_file)
