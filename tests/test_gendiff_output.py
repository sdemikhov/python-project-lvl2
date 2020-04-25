import pytest
from pathlib import Path

from gendiff.gendiff_lib import generate_diff


TESTS_DIR = Path(__file__).parent.absolute()
FIXTURES_DIR = TESTS_DIR / 'fixtures'

TEST_DATA = [
    (
        'simple1.json',
        'simple2.json',
        'nested',
    ),
    (
        'simple1.json',
        'simple1.json',
        'nested',
    ),
    (
        'simple1.json',
        'simple3.json',
        'nested',
    ),
    (
        'simple1.yaml',
        'simple2.yaml',
        'nested',
    ),
    (
        'simple1.yaml',
        'simple1.yaml',
        'nested',
    ),
    (
        'simple1.yaml',
        'simple3.yaml',
        'nested',
    ),
    (
        'complex1.json',
        'complex2.json',
        'nested',
    ),
    (
        'complex1.json',
        'complex1.json',
        'nested',
    ),
    (
        'complex1.json',
        'complex3.json',
        'nested',
    ),
    (
        'complex1.yaml',
        'complex2.yaml',
        'nested',
    ),
    (
        'complex1.yaml',
        'complex1.yaml',
        'nested',
    ),
    (
        'complex1.yaml',
        'complex3.yaml',
        'nested',
    ),
        (
        'simple1.json',
        'simple2.json',
        'plain',
    ),
    (
        'simple1.json',
        'simple1.json',
        'plain',
    ),
    (
        'simple1.json',
        'simple3.json',
        'plain',
    ),
    (
        'simple1.yaml',
        'simple2.yaml',
        'plain',
    ),
    (
        'simple1.yaml',
        'simple1.yaml',
        'plain',
    ),
    (
        'simple1.yaml',
        'simple3.yaml',
        'plain',
    ),
    (
        'complex1.json',
        'complex2.json',
        'plain',
    ),
    (
        'complex1.json',
        'complex1.json',
        'plain',
    ),
    (
        'complex1.json',
        'complex3.json',
        'plain',
    ),
    (
        'complex1.yaml',
        'complex2.yaml',
        'plain',
    ),
    (
        'complex1.yaml',
        'complex1.yaml',
        'plain',
    ),
    (
        'complex1.yaml',
        'complex3.yaml',
        'plain',
    ),
        (
        'simple1.json',
        'simple2.json',
        'json',
    ),
    (
        'simple1.json',
        'simple1.json',
        'json',
    ),
    (
        'simple1.json',
        'simple3.json',
        'json',
    ),
    (
        'simple1.yaml',
        'simple2.yaml',
        'json',
    ),
    (
        'simple1.yaml',
        'simple1.yaml',
        'json',
    ),
    (
        'simple1.yaml',
        'simple3.yaml',
        'json',
    ),
    (
        'complex1.json',
        'complex2.json',
        'json',
    ),
    (
        'complex1.json',
        'complex1.json',
        'json',
    ),
    (
        'complex1.json',
        'complex3.json',
        'json',
    ),
    (
        'complex1.yaml',
        'complex2.yaml',
        'json',
    ),
    (
        'complex1.yaml',
        'complex1.yaml',
        'json',
    ),
    (
        'complex1.yaml',
        'complex3.yaml',
        'json',
    ),
]


@pytest.mark.parametrize('file_name1,file_name2,output_format',
                         TEST_DATA)
def test_output_format(file_name1, file_name2, output_format):
    path_file1 = FIXTURES_DIR / file_name1
    path_file2 = FIXTURES_DIR / file_name2

    diff = generate_diff(path_file1, path_file2, output_format).split('\n')

    path_expected = (
        FIXTURES_DIR / '{f_name1}_{f_name2}_result_{output}_format.txt'.format(
            f_name1=file_name1.split('.')[0],
            f_name2=file_name2.split('.')[0],
            output=output_format,
        )
    )
    with open(path_expected) as f:
        expected = f.read().split('\n')
    
    assert len(diff) == len(expected), 'rows count must be equal'

    for row in expected:
        assert row in diff, 'must contain expected rows'
