# Given an N by N matrix, rotate it by 90 degrees clockwise.

# For example, given the following matrix:

# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]

# you should return:

# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]

# Extra space solution
def rotate(lst):
    ln = len(lst)
    rotate = list()
    for row in range(ln):
        r = list()
        for col in reversed(range(ln)):
            r.append(lst[col][row])
        rotate.append(r)
    return rotate

# Test
r = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

print(rotate(r))
