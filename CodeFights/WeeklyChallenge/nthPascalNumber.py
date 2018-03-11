# Given an integer n, find the nth number in Pascal's Triangle.

def nthPascalNumber(n):
    x = 1
    num_row = 0
    while x <= n:
        num_row += 1
        x += num_row
    pascal = []
    for r in range(num_row):
        newValue = 1
        pascal.append(newValue)
        for i in range(r):
            newValue = newValue * (r - i) * 1 / (i + 1)
            pascal.append(int(newValue))
    return pascal[n - 1]
