from gendiff import cli
from gendiff.file_loader import load_file


def run():
    arguments = cli.make_arguments()
    path_to_file1 = cli.get_path_to_file1(arguments)
    path_to_file2 = cli.get_path_to_file2(arguments)

    diff = generate_diff(path_to_file1, path_to_file2)
    print(diff, end='')


def generate_diff(path_to_file1, path_to_file2):
    data_file1 = load_file(path_to_file1)
    data_file2 = load_file(path_to_file2)

    difference = make_difference(data_file1, data_file2)

    return stringify_difference(
        difference,
        indent_level = 0,
        indent_type = '  '
    )


def make_difference(data_file1, data_file2):
    difference = {}

    keys_file1 = set(data_file1.keys())
    keys_file2 = set(data_file2.keys())

    shared_keys = keys_file1 & keys_file2
    unique_keys_file1 = keys_file1 - keys_file2
    unique_keys_file2 = keys_file2 - keys_file1
    
    for unique_key1 in unique_keys_file1:
        difference[unique_key1] = {
            'type': 'deleted_element',
            'value': data_file1[unique_key1],
        }

    for unique_key2 in unique_keys_file2:
        difference[unique_key2] = {
            'type': 'added_element',
            'value': data_file2[unique_key2],
        }

    for shared_key in shared_keys:
        if data_file1[shared_key] == data_file2[shared_key]:
            difference[shared_key] = {
            'type': 'unchanged_element',
            'value': data_file1[shared_key],
        }
        else:
            shared_values = (data_file1[shared_key], data_file2[shared_key])
            if all(isinstance(value, dict) for value in shared_values):
                difference[shared_key] = {
                    'type': 'container',
                    'value': make_difference(*shared_values),
                }
            else:
                difference[shared_key] = {
                    'type': 'edited_element',
                    'value': {
                        'before': data_file1[shared_key],
                        'after': data_file2[shared_key],
                    }
                }
    return difference


def stringify_difference(difference, indent_level, indent_type):
    indent = indent_type * indent_level
    result = '{indent}{{\n'.format(indent = indent)
    for key, value in difference.items():
        if value.get('type') == 'container':
            container = stringify_difference(
                value.get('value'),
                indent_level + 1,
                indent_type
            )
            element_as_string = '{indent}{key}: {container}'.format(
                indent=indent_type * (indent_level + 1),
                key=key,
                container=container,
            )
        elif value.get('type').endswith('unchanged_element'):
            element_as_string = stringify_unchanged_element(
                {key: value.get('value')},
                indent_type * (indent_level + 1)
            )
        elif value.get('type').endswith('edited_element'):
            element_as_string = stringify_edited_element(
                {key: value.get('value')},
                indent_type * (indent_level + 1)
            )
        elif value.get('type').endswith('deleted_element'):
            element_as_string = stringify_deleted_element(
                {key: value.get('value')},
                indent_type * (indent_level + 1)
            )
        elif value.get('type').endswith('added_element'):
            element_as_string = stringify_added_element(
                {key: value.get('value')},
                indent_type * (indent_level + 1)
            )
        result += element_as_string
    result += '{indent}}}\n'.format(indent = indent)
    return result


def stringify_unchanged_element(element, indent):
    template = '{indent}{key}: {value}\n'
    return element_to_string(element, template, indent)


def stringify_edited_element(element, indent):
    element_as_string = ''
    template = ('{indent}+ {key}: {after}\n{indent}- {key}: {before}\n')
    for key, value in element.items():
        before = value['before']
        after = value['after']
        element_as_string += template.format(
            indent=indent,
            key=key,
            before=before,
            after=after,
        )
    return element_as_string


def stringify_deleted_element(element, indent):
    template = '{indent}- {key}: {value}\n'
    return element_to_string(element, template, indent)


def stringify_added_element(element, indent):
    template = '{indent}+ {key}: {value}\n'
    return element_to_string(element, template, indent)


def element_to_string(element, template, indent):
    element_as_string = ''
    for key, value in element.items():
        element_as_string += template.format(indent=indent,key=key, value=value)
    return element_as_string
