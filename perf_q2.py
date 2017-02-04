from array import array
from time import time
from random import randrange

from q2 import exist_sum_center

def gen(sum_range, success=False):
    sum = randrange(*sum_range)

    left = get_sum_nums(sum)
    center = randrange(1, 10)
    if success:
        right = get_sum_nums(sum)
    else:
        right = get_sum_nums(randrange(*sum_range))

    return array('i', left + [center] + right)

def get_sum_nums(sum):
    num_list = []
    while True:
        n = int(randrange(1, sum) / randrange(1, 10000)) if sum > 1 else 1
        num_list.append(n)
        sum -= n
        if sum == 0:
            break
    return num_list

if __name__ == '__main__':
    print('performance: q2\n')
    gap_sum = 0
    for i in range(0, 10):
        num_array = gen((10**6, 10**7-1), randrange(0, 11)%2 == 0)

        before = time()

        exist_sum_center(num_array)

        gap = time() - before
        gap_sum += gap
        arr_size = len(num_array)
        print('run {0}:\ttime {1}, size {2}'.format(i + 1, gap, arr_size))
    
    print('\nq2 performance\n\tsum: {0}\n\tavg: {1}'.format(gap_sum, gap_sum / 10))