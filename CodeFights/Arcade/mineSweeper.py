# https://codefights.com/arcade/intro/level-5/ZMR5n7vJbexnLrgaM/description

# In the popular Minesweeper game you have a board with some mines and those cells
# that don't contain a mine have a number in it that indicates the total number of mines
# in the neighboring cells.

# Starting off with some arrangement of mines we want to create a Minesweeper game setup.

from copy import deepcopy

def minesweeper(matrix):
    m = deepcopy(matrix)
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == True:
                m[r][c] = count(r, c, matrix) - 1
            if matrix[r][c] == False:
                m[r][c] = count(r, c, matrix)
    return m

def count(r, c, matrix):
    count = 0
    for x in range(r-1, r+2):
        for y in range(c-1, c+2):
            if 0 <= y < len(matrix[0]) and 0 <= x < len(matrix):
                if matrix[x][y] == True:
                    count += 1
    return count
