import pytest
from pathlib import Path

from gendiff.gendiff_lib import generate_diff


TESTS_DIR = Path(__file__).parent.absolute()
FIXTURES_DIR = TESTS_DIR / 'fixtures'

PLAIN_JSON_DATA = [
    (
        FIXTURES_DIR / 'plain1.json',
        FIXTURES_DIR / 'plain2.json',
        FIXTURES_DIR / 'plain1_plain2_json_results.txt',
    ),
    (
        FIXTURES_DIR / 'plain1.json',
        FIXTURES_DIR / 'plain1.json',
        FIXTURES_DIR / 'plain1_plain1_json_results.txt',
    ),
    (
        FIXTURES_DIR / 'plain1.json',
        FIXTURES_DIR / 'plain3.json',
        FIXTURES_DIR / 'plain1_plain3_json_results.txt',
    ),
]


def get_file(path):
    with open(path) as f:
        return f.read()


@pytest.mark.parametrize('path_json1,path_json2,path_expected',
                         PLAIN_JSON_DATA)
def test_plain_json(path_json1, path_json2, path_expected):
    diff = generate_diff(path_json1, path_json2).split('\n')

    expected = get_file(path_expected).split('\n')

    assert len(diff) == len(expected), 'rows count must be equal'

    for row in expected:
        assert row in diff, 'must contain expected rows'
