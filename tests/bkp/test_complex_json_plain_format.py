import pytest
from pathlib import Path

from gendiff.gendiff_lib import generate_diff


TESTS_DIR = Path(__file__).parent.absolute()
FIXTURES_DIR = TESTS_DIR / 'fixtures'

COMPLEX_JSON_DATA = [
    (
        FIXTURES_DIR / 'complex1.json',
        FIXTURES_DIR / 'complex2.json',
        FIXTURES_DIR / 'complex1_complex2_result_plain_format.txt',
    ),
]


@pytest.mark.parametrize('path_json1,path_json2,path_expected',
                         COMPLEX_JSON_DATA)
def test_complex_json(path_json1, path_json2, path_expected):
    diff = generate_diff(path_json1, path_json2, 'plain').split('\n')

    with open(path_expected) as f:
        expected = f.read().split('\n')
    
    assert len(diff) == len(expected), 'rows count must be equal'

    for row in expected:
        assert row in diff, 'must contain expected rows'

def test_complex_json_no_changes():
    diff = generate_diff(
        FIXTURES_DIR / 'complex1.json',
        FIXTURES_DIR / 'complex1.json',
        'plain'
    )

    assert diff == '', 'must return empty line if no changes'
