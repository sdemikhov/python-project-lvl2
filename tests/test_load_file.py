import pytest
from pathlib import Path

from gendiff.file_loader import load_file


TESTS_DIR = Path(__file__).parent
FIXTURES_DIR = TESTS_DIR / 'fixtures'

JSON_PATH = {
    'absolute': FIXTURES_DIR.absolute() / 'plain1.json',
    'relative': FIXTURES_DIR / 'plain1.json',
}


YAML_PATH = {
    'absolute': FIXTURES_DIR.absolute() / 'plain1.yaml',
    'relative': FIXTURES_DIR / 'plain1.yaml',
}


TXT_PATH = {
    'absolute': FIXTURES_DIR.absolute() / 'plain1_plain1_results.txt',
    'relative': FIXTURES_DIR / 'plain1_plain1_results.txt',
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
