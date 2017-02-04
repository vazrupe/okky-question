from array import array

from util import get_nums


def exist_sum_center(num_array):
    array_size = len(num_array)
    if array_size <= 1:
        return True
    elif array_size == 2:
        return (num_array[0] == 0) or (num_array[1] == 0)

    idx = int(array_size / 2)

    left = sum(num_array[:idx])
    right = sum(num_array[idx+1:])

    sum_gap = right - left
    mov_size = int(idx/2)
    while True:
        if mov_size <= 0:
            return sum_gap == 0

        if sum_gap < 0: # left mov
            next_idx = idx - mov_size
            sum_gap += sum(num_array[next_idx+1:idx+1]) + num_array[next_idx]
            idx = next_idx
        elif sum_gap > 0: # right mov
            next_idx = idx + mov_size
            sum_gap -= sum(num_array[idx:next_idx]) + num_array[next_idx]
            idx = next_idx

        if sum_gap == 0:
            return True

        mov_size = int(mov_size/2)


if __name__ == '__main__':
    tc_num = int(input())

    for _ in range(tc_num):
        n = int(input())
        num_array = array('i', (i for i in get_nums(n)))
        
        print('YES' if exist_sum_center(num_array) else 'NO')
