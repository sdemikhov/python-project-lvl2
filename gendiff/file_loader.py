import json
import yaml


def load_file(path_to_file):
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
    with open(path_to_file) as json_file:
        return json.load(json_file)


def get_data_from_yaml(path_to_file):
    with open(path_to_file) as yaml_file:
        return yaml.safe_load(yaml_file)
