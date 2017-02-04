from q1 import get_gap_list


def test_get_gap_list():
    test_list = [1,2,3,4,5,6,7,8,9,10]
    gap = 3
    result = [
        (1, 4), 
        (2, 5),
        (3, 6),
        (4, 7),
        (5, 8),
        (6, 9),
        (7, 10),
    ]
    assert [i for i in get_gap_list(test_list, gap)] == result