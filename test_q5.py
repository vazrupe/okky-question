from q5 import (
    next_dict_str, 
    exist_next_dict_str
)


def test_next_dict_str():
    assert next_dict_str('ab') == 'ba'
    assert next_dict_str('bb') is None
    assert next_dict_str('hefg') == 'hegf'


def test_exist_next_dict_str():
    assert exist_next_dict_str('abc')
    assert not exist_next_dict_str('cba')
    assert exist_next_dict_str('cab')
    assert not exist_next_dict_str('aaa')
    assert not exist_next_dict_str('aa')
    assert not exist_next_dict_str('a')