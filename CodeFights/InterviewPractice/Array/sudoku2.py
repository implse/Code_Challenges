# https://codefights.com/interview-practice/task/SKZ45AF99NpbnvgTn/description

# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with
# numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids
# that compose the grid all contain all of the numbers from 1 to 9 one time.
#
# Implement an algorithm that will check whether the given grid of numbers represents
# a valid Sudoku puzzle according to the layout rules described above.
# Note that the puzzle represented by grid does not have to be solvable.

def sudoku2(grid):
    ln_row = len(grid)
    ln_col = len(grid[0])
    # row check
    for r in range(ln_row):
        if check_line(grid[r]) != True:
            return False
    # column check
    for c in range(ln_col):
        line = []
        for r in range(ln_row):
            line.append(grid[r][c])
        if check_line(line) != True:
            return False
    # 9 cubes to check
    l = 0
    while l < 9:
        k = 0
        while k < 9:
            line = []
            for y in range(k, k + 3):
                for x in range(l, l + 3):
                    line.append(grid[y][x])
            k += 3
            if check_line(line) != True:
                return False
        l += 3
    return True

def check_line(line):
    check_num = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
    for l in line:
        if l != '.':
            check_num[l] += 1
            if check_num[l] > 1:
                return False
    return True
