import pytest

from lectures.dictionaries.roman_numbers import solution


@pytest.mark.parametrize("input,expected", [
    ('XXI', 21),
    ('I', 1),
    ('IV', 4),
    ('MMVIII', 2008),
    ('MDCLXVI', 1666)])
def test_all_cases(input, expected):
    assert solution(input) == expected