import sys
import io

from util import get_nums


def test_get_nums():
    sys.stdin = io.StringIO('12 10')
    assert [num for num in get_nums(2)] == [12, 10]

    sys.stdin = io.StringIO('12 1')
    assert [num for num in get_nums(2)] != [12, 10]
