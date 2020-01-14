# https://app.codesignal.com/interview-practice/task/C8Jdyk3ybixqQdAvM

def strstr(s, x):
    # Boyer Moore Algorithm
    table = dict()
    for index, char in enumerate(x):
        table[char] = max(1, len(x) - index - 1)

    index = 0
    offset = 0
    while len(s) - offset >= len(x):
        i = len(x) - 1
        while s[offset + i] == x[i]:
            if i == 0:
                return offset
            i -= 1
        offset += table.get(s[offset + len(x) - 1], len(x))
    return -1
