from gendiff import cli
from gendiff.file_loader import load_file


def run():
    arguments = cli.make_arguments()
    path_to_file1 = cli.get_path_to_file1(arguments)
    path_to_file2 = cli.get_path_to_file2(arguments)

    diff = generate_diff(path_to_file1, path_to_file2)
    print(diff, end='')


def generate_diff(path_to_file1, path_to_file2):
    file1 = load_file(path_to_file1)
    file2 = load_file(path_to_file2)

    difference = make_difference(file1, file2)

    return format_difference_plain(difference)


def make_difference(file1, file2):
    difference = {
        'same': {},
        'edited': {},
        'deleted': {},
        'added': {},
    }

    keys_file1 = set(file1.keys())
    keys_file2 = set(file2.keys())

    shared_keys = keys_file1 & keys_file2
    unique_keys_file1 = keys_file1 - keys_file2
    unique_keys_file2 = keys_file2 - keys_file1

    for shared_key in shared_keys:
        if file1[shared_key] == file2[shared_key]:
            difference['same'][shared_key] = file1[shared_key]
        else:
            difference['edited'][shared_key] = {
                'before': file1[shared_key],
                'after': file2[shared_key],
            }

    for unique_key1 in unique_keys_file1:
        difference['deleted'][unique_key1] = file1[unique_key1]

    for unique_key2 in unique_keys_file2:
        difference['added'][unique_key2] = file2[unique_key2]

    return difference


def get_same_fields(difference):
    return difference['same']


def get_edited_fields(difference):
    return difference['edited']


def get_deleted_fields(difference):
    return difference['deleted']


def get_added_fields(difference):
    return difference['added']


def format_difference_plain(difference):
    template = '{{\n{same}{edited}{deleted}{added}}}\n'

    same = stringify_same_fields(get_same_fields(difference))
    edited = stringify_edited_fields(get_edited_fields(difference))
    deleted = stringify_deleted_fields(get_deleted_fields(difference))
    added = stringify_added_fields(get_added_fields(difference))

    return template.format(
        same=same,
        edited=edited,
        deleted=deleted,
        added=added,
    )


def stringify_same_fields(fields):
    template = '    {key}: {value}\n'
    return fields_to_string(fields, template)


def stringify_edited_fields(fields):
    fields_as_string = ''
    template = ('  + {key}: {after}\n  - {key}: {before}\n')
    for key, value in fields.items():
        before = value['before']
        after = value['after']
        fields_as_string += template.format(
            key=key,
            before=before,
            after=after,
        )
    return fields_as_string


def stringify_deleted_fields(fields):
    template = '  - {key}: {value}\n'
    return fields_to_string(fields, template)


def stringify_added_fields(fields):
    template = '  + {key}: {value}\n'
    return fields_to_string(fields, template)


def fields_to_string(fields, template):
    fields_as_string = ''
    for key, value in fields.items():
        fields_as_string += template.format(key=key, value=value)
    return fields_as_string
