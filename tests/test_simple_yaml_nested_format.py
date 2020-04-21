import pytest
from pathlib import Path

from gendiff.gendiff_lib import generate_diff


TESTS_DIR = Path(__file__).parent.absolute()
FIXTURES_DIR = TESTS_DIR / 'fixtures'

PLAIN_YAML_DATA = [
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
]


@pytest.mark.parametrize('path_yaml1,path_yaml2,path_expected',
                         PLAIN_YAML_DATA)
def test_simple_yaml(path_yaml1, path_yaml2, path_expected):
    diff = generate_diff(path_yaml1, path_yaml2).split('\n')

    with open(path_expected) as f:
        expected = f.read().split('\n')

    assert len(diff) == len(expected), 'rows count must be equal'

    for row in expected:
        assert row in diff, 'must contain expected rows'


def test_edited_fields_yaml():
    diff = generate_diff(
        FIXTURES_DIR / 'simple1.yaml',
        FIXTURES_DIR / 'simple2.yaml'
    )

    expected = "  + timeout: 20\n  - timeout: 50"

    assert expected in diff, 'edited fields should be together'
