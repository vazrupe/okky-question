from functools import reduce


def next_dict_str(w):
    if not exist_next_dict_str(w):
        return None
    s = w[::-1]

    switch_ok = False
    str_size = len(s)
    for i in range(str_size - 1):
        for j in range(i + 1, str_size):
            if s[i] > s[j]:
                tmp = [c for c in s]
                tmp[i], tmp[j] = (tmp[j], tmp[i])
                s = ''.join(tmp)
                switch_ok = True
                break
        if switch_ok:
            break

    return s[::-1]

def exist_next_dict_str(w):
    str_size = len(w)
    if str_size < 2:
        return False
    for i in range(str_size - 1):
        if w[i] < w[i+1]:
            return True
    return False

if __name__ == '__main__':
    t = int(input())

    lines = []
    for _ in range(t):
        lines.append(input())

    for s in map(next_dict_str, lines):
        print(s if s else 'no answer')