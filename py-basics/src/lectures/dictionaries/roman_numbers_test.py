from lectures.dictionaries.roman_numbers import solution


def test1():
    assert solution('XXI') == 21


def test2():
    assert solution('I') == 1


def test3():
    assert solution('IV') == 4


def test4():
    assert solution('MMVIII') == 2008


def test5():
    assert solution('MDCLXVI') == 1666
