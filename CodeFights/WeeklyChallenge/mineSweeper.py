# https://codefights.com/challenge/48o3YSHdmHtWRTxNT

# In the popular Minesweeper game you have a board with some mines and those cells
# that don't contain a mine have a number in it that indicates the total number of
# mines in the neighboring cells.
# Starting off with some arrangement of mines we want to create a Minesweeper game setup.


import copy

def minesweeper(matrix):
    new_m = copy.deepcopy(matrix[:])
    ln_r = len(matrix)
    ln_c = len(matrix[0])
    for r in range(ln_r):
        for c in range(ln_c):
            b = 0
            for x in range(r - 1, r + 2):
                for y in range(c - 1, c + 2):
                    if 0 <= x < ln_r and 0 <= y < ln_c:
                        if matrix[x][y] == True:
                            b += 1
                if matrix[r][c] == True:
                    new_m[r][c] = b - 1
                else:
                    new_m[r][c] = b
    return new_m
