from array import array
import bisect

from util import get_nums


def get_gap_list(sorted_nums, gap):
    max_check_num = sorted_nums[-1] - gap

    for i in range(len(sorted_nums)):
        this_num = sorted_nums[i]
        if this_num > max_check_num:
            return

        target_num = this_num + gap
        for j in range(i, len(sorted_nums)):
            next_num = sorted_nums[j]
            if target_num == next_num:
                yield (this_num, next_num)
            elif target_num < next_num:
                break
                

if __name__ == '__main__':
    n, k = input().split(' ')
    n = int(n)
    k = int(k)

    num_array = array('i', ())
    for num in get_nums(n):
        bisect.insort(num_array, num)

    for i, j in get_gap_list(num_array, k):
        print(i, j)