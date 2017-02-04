from util import get_nums


class NineZeroGenerator:
    cache = []

    def __getitem__(self, key):
        cached_size = len(NineZeroGenerator.cache)
        if cached_size <= key:
            NineZeroGenerator.cache += list(map(
                self.make_nine_zero_num, 
                range(cached_size, key+1)
            ))
        return NineZeroGenerator.cache[key]

    def make_nine_zero_num(self, idx):
        return int('{0:b}'.format(idx + 1)) * 9


def find_multiple_num(num):
    i = 0
    gen = NineZeroGenerator()
    while True:
        nine_zero_num = gen[i]
        if nine_zero_num%num == 0:
            return nine_zero_num
        i += 1


if __name__ == '__main__':
    t = int(input())

    for n in map(find_multiple_num, [n for n in get_nums(t)]):
        print(find_multiple_num(n))
        