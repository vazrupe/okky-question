from array import array
from time import time
from random import randrange

from q1 import get_gap_list

def gen():
    max_count = 10**6
    num_range = (1, max_count * 100)

    num_array = array('i', set([randrange(*num_range) for i in range(1, max_count + 1)]))
    num_array = array(num_array.typecode, num_array)
    k = 10**randrange(2, 3)

    return num_array, k

if __name__ == '__main__':
    print('performance: q1\n')
    gap_sum = 0
    for i in range(0, 10):
        num_array, k = gen()

        before = time()
        for _ in get_gap_list(num_array, k):
            pass
        gap = time() - before
        gap_sum += gap
        print('run {0}:\ttime {1}'.format(i + 1, gap))
    
    print('\nq1 performance\n\tsum: {0}\n\tavg: {1}'.format(gap_sum, gap_sum / 10))
