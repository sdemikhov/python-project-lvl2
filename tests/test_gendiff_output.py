import pytest
from pathlib import Path
import json

from gendiff.generate_diff import generate_diff


TESTS_DIR = Path(__file__).parent.absolute()
FIXTURES_DIR = TESTS_DIR / 'fixtures'

FILENAME_EXTENSIONS = (
    '.json',
    '.yaml',
)

TEXT_FORMAT_RESULT = 'result*.txt'
JSON_FORMAT_RESULT = 'result*.json'

def make_test_data(glob_expression):
    test_data = []
    for expected in FIXTURES_DIR.glob(glob_expression):
        _, filename1, filename2, format = expected.stem.split('_')
        for extension in FILENAME_EXTENSIONS:
            test_data.append(
                (
                    expected.name,
                    FIXTURES_DIR / (filename1 + extension),
                    FIXTURES_DIR / (filename2 + extension),
                    format,
                )
            )
    return test_data


@pytest.mark.parametrize('expected,file_name1,file_name2,output_format',
                         make_test_data(TEXT_FORMAT_RESULT))
def test_text_formats(expected, file_name1, file_name2, output_format):
    path_file1 = file_name1
    path_file2 = file_name2

    diff = generate_diff(path_file1, path_file2, output_format).split('\n')

    path_expected = FIXTURES_DIR / expected

    with open(path_expected) as f:
        expected = f.read().split('\n')
    
    assert diff == expected, 'diff must be exact as the reference value'


@pytest.mark.parametrize('expected,file_name1,file_name2,output_format',
                         make_test_data(JSON_FORMAT_RESULT))
def test_json_format(expected, file_name1, file_name2, output_format):
    path_file1 = file_name1
    path_file2 = file_name2

    diff = json.loads(generate_diff(path_file1, path_file2, output_format))

    path_expected = FIXTURES_DIR / expected

    with open(path_expected) as f:
        expected = json.load(f)
    
    assert diff == expected, 'diff must be exact as the reference value'
