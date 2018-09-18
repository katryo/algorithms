# https://www.youtube.com/watch?v=PHXAOKQk2dw

def kmp(text, pattern):
    def generate_table(ptn):
        tbl = [0] * len(ptn)
        left = 0
        for right in range(1, len(ptn)):
            tbl[right] = left
            if ptn[left] == ptn[right]:
                left += 1
            else:
                left = 0
        return tbl

    table = generate_table(pattern)

    cur = 0
    ptn_p = 0
    while cur < len(text) and ptn_p < len(pattern):
        if text[cur] == pattern[ptn_p]:
            cur += 1
            ptn_p += 1
        elif ptn_p == 0:
            cur += 1
        else:
            ptn_p = table[ptn_p]
    if ptn_p == len(pattern):
        return cur - len(pattern)
    return -1


def bmh(text, pattern):
    table = {}
    length = len(pattern)
    for i, char in enumerate(pattern):
        table[char] = length - i - 1

    def count_to_move(text_rightmost):
        if text_rightmost in table:
            return max(1, table[text_rightmost])
        else:
            return length

    cur = 0
    while cur <= len(text)-len(pattern):
        # cur_end = cur + len(pattern) - 1
        found = True
        to_move = count_to_move(text[cur+len(pattern)-1])
        if text[cur+len(pattern)-1] != pattern[len(pattern)-1]:
            cur += to_move
            continue
        for i in range(len(pattern)-2, -1, -1):
            if text[cur+i] != pattern[i]:
                found = False
                cur += to_move
                break
        if found:
            return cur
    return -1


def bm(text, pattern):
    table = {}
    length = len(pattern)
    for i, char in enumerate(pattern):
        table[char] = length - i - 1

    cur = 0
    while cur <= len(text)-len(pattern):
        found = True
        for i in range(len(pattern)-1, -1, -1):
            if text[cur+i] != pattern[i]:
                found = False
                if text[cur+i] in table:
                    cur += max(1, table[text[cur+i]])
                else:
                    cur += length
                break
        if found:
            return cur
    return -1


def naive(text, pattern):
    cur = 0
    while cur <= len(text)-len(pattern):
        found = True
        for i in range(len(pattern)):
            if text[cur+i] != pattern[i]:
                found = False
                break
        if found:
            return cur
        cur += 1
    return -1


if __name__ == '__main__':
    text = 'abcabcabcdabc'
    pattern = 'abcdabc'
    print(naive(text, pattern))
    print(bm(text, pattern))
    print(bmh(text, pattern))
    print(kmp(text, pattern))



