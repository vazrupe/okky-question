from q2 import exist_sum_center 


def test_exist_sum_center():
    assert exist_sum_center([1, 2, 3, 4, 6])
    assert exist_sum_center([6, 4, 3, 2, 1])
    
    assert not exist_sum_center([1, 2, 3])
    assert not exist_sum_center([3, 2, 1])

    assert exist_sum_center([1, 3, 2, 4])
    assert not exist_sum_center([1, 3, 2, 3])

    assert exist_sum_center([0])

    assert exist_sum_center([0, 1])
    assert exist_sum_center([1, 0])
    