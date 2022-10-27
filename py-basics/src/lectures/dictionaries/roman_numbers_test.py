from lectures.dictionaries.roman_numbers import solution


def test_case1():
    assert solution('XXI') == 21


def test_case2():
    assert solution('I') == 1


def test_case3():
    assert solution('IV') == 4


def test_case4():
    assert solution('MMVIII') == 2008


def test_case5():
    assert solution('MDCLXVI') == 1666
