from q3 import (
    NineZeroGenerator,
    find_multiple_num
)


def test_nine_zero_generator():
    gen = NineZeroGenerator()
    assert gen[0] == 9
    assert gen[3] == 900
    assert gen[150] == 90090999


def test_find_multiple_num():
    assert find_multiple_num(1) == 9
    assert find_multiple_num(10) == 90
    assert find_multiple_num(246) == 999990
    