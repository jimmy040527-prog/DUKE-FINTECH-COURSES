import pytest
from clock import MyClock24


def test_create():
    """ test creation """
    a = MyClock24(1, 5, 30)
    assert str(a) == "01:05:30"


def test_create_errors():
    """ test creation with bad ranges"""
    with pytest.raises(ValueError):
        MyClock24(25, 5, 30)

    with pytest.raises(ValueError):
        MyClock24(5, 65, 30)

    with pytest.raises(ValueError):
        MyClock24(5, 5, 95)

    with pytest.raises(ValueError):
        MyClock24(-1, 5, 30)

    with pytest.raises(ValueError):
        MyClock24(5, -1, 30)

    with pytest.raises(ValueError):
        MyClock24(5, 5, -1)


def test_str():
    """ test __str__ works correctly - formatting """
    a = MyClock24(7, 7, 7)
    assert str(a) == "07:07:07"

    b = MyClock24(23, 59, 59)
    assert str(b) == "23:59:59"


def test_repr():
    """ testing __repr__ """
    import ast

    b = MyClock24(23, 59, 58)
    assert ast.literal_eval(repr(b)) == {'hours': 23, 'minutes': 59, 'seconds': 58}


def test_properties():
    """ test access comparisons """
    a = MyClock24(23, 59, 58)
    assert a.hours == 23
    assert a.minutes == 59
    assert a.seconds == 58


def test_comparisons():
    """ test that the magic methods implemented for comparisons """
    a = MyClock24(23, 59, 58)
    b = MyClock24(23, 59, 58)
    c = MyClock24(0, 0, 0)

    assert a == b
    assert not (a == c)

    assert not (a != b)
    assert a != c

    assert a > c
    assert a >= b

    assert c < a
    assert b <= a


def test_arithmetic():
    """ test arithmetic """
    a = MyClock24(23, 59, 58)
    b = a + 3
    assert str(b) == "00:00:01"
    c = b - 3
    assert a == c

    b = MyClock24(0, 0, 3)
    c = a + b
    assert str(c) == "00:00:01"
    d = c - b
    assert a == d


def test_tick():
    """ test tick()"""
    a = MyClock24(23, 59, 0)
    for i in range(70):
        a.tick()
    assert str(a) == "00:00:10"
