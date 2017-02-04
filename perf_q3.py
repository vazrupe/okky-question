from time import time

from q3 import find_multiple_num

if __name__ == '__main__':
    print('performance: q3\n')
    before = time()
    case = 500
    for i in range(1, case + 1):
        find_multiple_num(i)
    gap = time() - before
    print('q3 performance\n\t1 ~ {0} case: {1}'.format(case, gap))