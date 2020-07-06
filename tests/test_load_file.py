import pytest
from pathlib import Path

from gendiff.file import load


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
    'absolute': FIXTURES_DIR.absolute() / 'result_simple1_simple1_default.txt',
    'relative': FIXTURES_DIR / 'result_simple1_simple1_default.txt',
}

def test_different_paths():    
    assert load(JSON_PATH['absolute']), (
        'must work with absolute path'
    )

    assert load(JSON_PATH['relative']), (
        'must work with relative path'
    )

    assert load(YAML_PATH['absolute']), (
        'must work with absolute path'
    )

    assert load(YAML_PATH['relative']), (
        'must work with relative path'
    )


def test_wrong_file():
    with pytest.raises(ValueError):
        load(TXT_PATH['absolute'])

    with pytest.raises(ValueError):
        load(TXT_PATH['relative'])
