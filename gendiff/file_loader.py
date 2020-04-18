# -*- coding: utf-8 -*-

"""The file_loader module provides functions for file loading."""


import json
import yaml


def load_file(path_to_file):
    """Return content of a YAML/JOSON file as python object.

    Keyword arguments:
    path_to_file -- specifies a unique location in a file system
    """
    try:
        data_from_yaml = get_data_from_yaml(path_to_file)
        return data_from_yaml
    except (yaml.scanner.ScannerError, yaml.parser.ParserError):
        try:
            data_from_json = get_data_from_json(path_to_file)
            return data_from_json
        except json.decoder.JSONDecodeError:
            raise(ValueError(
                'Error trying to load the file: {}'.format(path_to_file)
            ))


def get_data_from_json(path_to_file):
    """Load json file and return content as python object.

    Keyword arguments:
    path_to_file -- specifies a unique location in a file system
    """
    with open(path_to_file) as json_file:
        return json.load(json_file)


def get_data_from_yaml(path_to_file):
    """Load json file and return content as python object.

    Keyword arguments:
    path_to_file -- specifies a unique location in a file system
    """
    with open(path_to_file) as yaml_file:
        return yaml.safe_load(yaml_file)
