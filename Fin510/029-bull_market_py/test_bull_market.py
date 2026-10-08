from bull_market import find_longest_period


def test_norma_case():
    prices = [1, 2, 3, 1, 4, 5, 6, 7]
    assert find_longest_period(prices) == [1, 4, 5, 6, 7]


def test_same_length_returns_first():
    prices = [1, 2, 3, 0, 4, 5]
    assert find_longest_period(prices) == [1, 2, 3]


def test_decreasing_case():
    prices = [5, 4, 3]
    assert find_longest_period(prices) == [5]


def test_invalid_type_not_int_or_float():
    prices = [1, 2, "1", 4]

    try:
        find_longest_period(prices)
        assert False
    except TypeError:
        assert True