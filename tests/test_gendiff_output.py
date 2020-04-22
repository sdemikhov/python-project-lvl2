import pytest
from pathlib import Path

from gendiff.gendiff_lib import generate_diff


TESTS_DIR = Path(__file__).parent.absolute()
FIXTURES_DIR = TESTS_DIR / 'fixtures'

TEST_DATA_NESTED_FORMAT = [
    (
        FIXTURES_DIR / 'simple1.json',
        FIXTURES_DIR / 'simple2.json',
        FIXTURES_DIR / 'simple1_simple2_result_nested_format.txt',
    ),
    (
        FIXTURES_DIR / 'simple1.json',
        FIXTURES_DIR / 'simple1.json',
        FIXTURES_DIR / 'simple1_simple1_result_nested_format.txt',
    ),
    (
        FIXTURES_DIR / 'simple1.json',
        FIXTURES_DIR / 'simple3.json',
        FIXTURES_DIR / 'simple1_simple3_result_nested_format.txt',
    ),
    (
        FIXTURES_DIR / 'simple1.yaml',
        FIXTURES_DIR / 'simple2.yaml',
        FIXTURES_DIR / 'simple1_simple2_result_nested_format.txt',
    ),
    (
        FIXTURES_DIR / 'simple1.yaml',
        FIXTURES_DIR / 'simple1.yaml',
        FIXTURES_DIR / 'simple1_simple1_result_nested_format.txt',
    ),
    (
        FIXTURES_DIR / 'simple1.yaml',
        FIXTURES_DIR / 'simple3.yaml',
        FIXTURES_DIR / 'simple1_simple3_result_nested_format.txt',
    ),
    (
        FIXTURES_DIR / 'complex1.json',
        FIXTURES_DIR / 'complex2.json',
        FIXTURES_DIR / 'complex1_complex2_result_nested_format.txt',
    ),
    (
        FIXTURES_DIR / 'complex1.json',
        FIXTURES_DIR / 'complex1.json',
        FIXTURES_DIR / 'complex1_complex1_result_nested_format.txt',
    ),
    (
        FIXTURES_DIR / 'complex1.json',
        FIXTURES_DIR / 'complex3.json',
        FIXTURES_DIR / 'complex1_complex3_result_nested_format.txt',
    ),
    (
        FIXTURES_DIR / 'complex1.yaml',
        FIXTURES_DIR / 'complex2.yaml',
        FIXTURES_DIR / 'complex1_complex2_result_nested_format.txt',
    ),
    (
        FIXTURES_DIR / 'complex1.yaml',
        FIXTURES_DIR / 'complex1.yaml',
        FIXTURES_DIR / 'complex1_complex1_result_nested_format.txt',
    ),
    (
        FIXTURES_DIR / 'complex1.yaml',
        FIXTURES_DIR / 'complex3.yaml',
        FIXTURES_DIR / 'complex1_complex3_result_nested_format.txt',
    ),
]


@pytest.mark.parametrize('path_file1,path_file2,path_expected',
                         TEST_DATA_NESTED_FORMAT)
def test_nested_format(path_file1, path_file2, path_expected):
    diff = generate_diff(path_file1, path_file2, 'nested').split('\n')

    with open(path_expected) as f:
        expected = f.read().split('\n')
    
    assert len(diff) == len(expected), 'rows count must be equal'

    for row in expected:
        assert row in diff, 'must contain expected rows'


TEST_DATA_PLAIN_FORMAT = [
    (
        FIXTURES_DIR / 'simple1.json',
        FIXTURES_DIR / 'simple2.json',
        FIXTURES_DIR / 'simple1_simple2_result_plain_format.txt',
    ),
    (
        FIXTURES_DIR / 'simple1.json',
        FIXTURES_DIR / 'simple1.json',
        FIXTURES_DIR / 'simple1_simple1_result_plain_format.txt',
    ),
    (
        FIXTURES_DIR / 'simple1.json',
        FIXTURES_DIR / 'simple3.json',
        FIXTURES_DIR / 'simple1_simple3_result_plain_format.txt',
    ),
    (
        FIXTURES_DIR / 'simple1.yaml',
        FIXTURES_DIR / 'simple2.yaml',
        FIXTURES_DIR / 'simple1_simple2_result_plain_format.txt',
    ),
    (
        FIXTURES_DIR / 'simple1.yaml',
        FIXTURES_DIR / 'simple1.yaml',
        FIXTURES_DIR / 'simple1_simple1_result_plain_format.txt',
    ),
    (
        FIXTURES_DIR / 'simple1.yaml',
        FIXTURES_DIR / 'simple3.yaml',
        FIXTURES_DIR / 'simple1_simple3_result_plain_format.txt',
    ),
    (
        FIXTURES_DIR / 'complex1.json',
        FIXTURES_DIR / 'complex2.json',
        FIXTURES_DIR / 'complex1_complex2_result_plain_format.txt',
    ),
    (
        FIXTURES_DIR / 'complex1.json',
        FIXTURES_DIR / 'complex1.json',
        FIXTURES_DIR / 'complex1_complex1_result_plain_format.txt',
    ),
    (
        FIXTURES_DIR / 'complex1.json',
        FIXTURES_DIR / 'complex3.json',
        FIXTURES_DIR / 'complex1_complex3_result_plain_format.txt',
    ),
    (
        FIXTURES_DIR / 'complex1.yaml',
        FIXTURES_DIR / 'complex2.yaml',
        FIXTURES_DIR / 'complex1_complex2_result_plain_format.txt',
    ),
    (
        FIXTURES_DIR / 'complex1.yaml',
        FIXTURES_DIR / 'complex1.yaml',
        FIXTURES_DIR / 'complex1_complex1_result_plain_format.txt',
    ),
    (
        FIXTURES_DIR / 'complex1.yaml',
        FIXTURES_DIR / 'complex3.yaml',
        FIXTURES_DIR / 'complex1_complex3_result_plain_format.txt',
    ),
]


@pytest.mark.parametrize('path_file1,path_file2,path_expected',
                         TEST_DATA_PLAIN_FORMAT)
def test_plain_format(path_file1, path_file2, path_expected):
    diff = generate_diff(path_file1, path_file2, 'plain').split('\n')

    with open(path_expected) as f:
        expected = f.read().split('\n')
    
    assert len(diff) == len(expected), 'rows count must be equal'

    for row in expected:
        assert row in diff, 'must contain expected rows'


TEST_DATA_JSON_FORMAT = [
    (
        FIXTURES_DIR / 'simple1.json',
        FIXTURES_DIR / 'simple2.json',
        FIXTURES_DIR / 'simple1_simple2_result_json_format.txt',
    ),
    (
        FIXTURES_DIR / 'simple1.json',
        FIXTURES_DIR / 'simple1.json',
        FIXTURES_DIR / 'simple1_simple1_result_json_format.txt',
    ),
    (
        FIXTURES_DIR / 'simple1.json',
        FIXTURES_DIR / 'simple3.json',
        FIXTURES_DIR / 'simple1_simple3_result_json_format.txt',
    ),
    (
        FIXTURES_DIR / 'simple1.yaml',
        FIXTURES_DIR / 'simple2.yaml',
        FIXTURES_DIR / 'simple1_simple2_result_json_format.txt',
    ),
    (
        FIXTURES_DIR / 'simple1.yaml',
        FIXTURES_DIR / 'simple1.yaml',
        FIXTURES_DIR / 'simple1_simple1_result_json_format.txt',
    ),
    (
        FIXTURES_DIR / 'simple1.yaml',
        FIXTURES_DIR / 'simple3.yaml',
        FIXTURES_DIR / 'simple1_simple3_result_json_format.txt',
    ),
    (
        FIXTURES_DIR / 'complex1.json',
        FIXTURES_DIR / 'complex2.json',
        FIXTURES_DIR / 'complex1_complex2_result_json_format.txt',
    ),
    (
        FIXTURES_DIR / 'complex1.json',
        FIXTURES_DIR / 'complex1.json',
        FIXTURES_DIR / 'complex1_complex1_result_json_format.txt',
    ),
    (
        FIXTURES_DIR / 'complex1.json',
        FIXTURES_DIR / 'complex3.json',
        FIXTURES_DIR / 'complex1_complex3_result_json_format.txt',
    ),
    (
        FIXTURES_DIR / 'complex1.yaml',
        FIXTURES_DIR / 'complex2.yaml',
        FIXTURES_DIR / 'complex1_complex2_result_json_format.txt',
    ),
    (
        FIXTURES_DIR / 'complex1.yaml',
        FIXTURES_DIR / 'complex1.yaml',
        FIXTURES_DIR / 'complex1_complex1_result_json_format.txt',
    ),
    (
        FIXTURES_DIR / 'complex1.yaml',
        FIXTURES_DIR / 'complex3.yaml',
        FIXTURES_DIR / 'complex1_complex3_result_json_format.txt',
    ),
]


@pytest.mark.parametrize('path_file1,path_file2,path_expected',
                         TEST_DATA_JSON_FORMAT)
def test_json_format(path_file1, path_file2, path_expected):
    diff = generate_diff(path_file1, path_file2, 'json').split('\n')

    with open(path_expected) as f:
        expected = f.read().split('\n')
    
    assert len(diff) == len(expected), 'rows count must be equal'

    for row in expected:
        assert row in diff, 'must contain expected rows'
