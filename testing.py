import os
import pytest
from main import find_partial_matches

@pytest.fixture(scope="module")
def s1_content():
    return [
        'cat',
        'dog',
        'mouse',
        'rabbit',
        'elephant',
        'duo',
        'mum'
    ]

@pytest.fixture(scope="module")
def s2_content():
    return [
        'cot',
        'fog',
        'mousse',
        'raccoon',
        'hippopotamus',
        'dea',
        'mtm'
    ]

def test_find_partial_matches(s1_content, s2_content):
    result = find_partial_matches(s1_content, s2_content)
    expected_result = [
        {'s1': 'cat', 's2': 'cot', 'distance': 1},
        {'s1': 'dog', 's2': 'fog', 'distance': 1},
        {'s1': 'mouse', 's2': 'mousse', 'distance': 1},
        {'s1': 'dog', 's2': 'cot', 'distance': 2},
        {'s1': 'duo', 's2': 'dea', 'distance': 2},
        {'s1': 'dog', 's2': 'dea', 'distance': 2},
        {'s1': 'mum', 's2': 'mtm', 'distance': 1},
    ]
    assert len(result) == len(expected_result), f"Expected {len(expected_result)} matches, but got {len(result)}"

    for item in expected_result:
        assert item in result, f"Expected {item} not found in result"