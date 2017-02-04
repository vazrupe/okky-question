import sys

def get_nums(count):
    i = 0
    while i < count:
        num = ''
        while True:
            chr = sys.stdin.read(1)
            if not('0' <= chr <= '9'):
                break
            num += chr
        yield int(num)
        i += 1

if __name__ == '__main__':
    for num in get_nums(2):
        print(num)
