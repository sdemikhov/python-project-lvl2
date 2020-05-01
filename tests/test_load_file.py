import pytest
from pathlib import Path

from gendiff.load_file import load_file


TESTS_DIR = Path(__file__).parent
FIXTURES_DIR = TESTS_DIR / 'fixtures'

JSON_PATH = {
    'absolute': FIXTURES_DIR.absolute() / 'simple1.json',
    'relative': FIXTURES_DIR / 'simple1.json',
}


YAML_PATH = {
    'absolute': FIXTURES_DIR.absolute() / 'simple1.yaml',
    'relative': FIXTURES_DIR / 'simple1.yaml',
}


TXT_PATH = {
    'absolute': FIXTURES_DIR.absolute() / 'simple1_simple1_result_default_format.txt',
    'relative': FIXTURES_DIR / 'simple1_simple1_result_default_format.txt',
}

def test_different_paths():    
    assert load_file(JSON_PATH['absolute']), (
        'must work with absolute path'
    )

    assert load_file(JSON_PATH['relative']), (
        'must work with relative path'
    )

    assert load_file(YAML_PATH['absolute']), (
        'must work with absolute path'
    )

    assert load_file(YAML_PATH['relative']), (
        'must work with relative path'
    )


def test_wrong_file():
    with pytest.raises(ValueError):
        load_file(TXT_PATH['absolute'])

    with pytest.raises(ValueError):
        load_file(TXT_PATH['relative'])
