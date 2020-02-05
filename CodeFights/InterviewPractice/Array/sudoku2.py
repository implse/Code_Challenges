# https://codefights.com/interview-practice/task/SKZ45AF99NpbnvgTn/description

# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with
# numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids
# that compose the grid all contain all of the numbers from 1 to 9 one time.
#
# Implement an algorithm that will check whether the given grid of numbers represents
# a valid Sudoku puzzle according to the layout rules described above.
# Note that the puzzle represented by grid does not have to be solvable.

def sudoku2(grid):
    #check rows
    for row in range(len(grid)):
        row_map = dict()
        for col in range(len(grid[0])):
            if grid[row][col] in row_map.keys():
                return False
            else:
                if grid[row][col] != ".":
                    row_map[grid[row][col]] = 1

    # check cols
    for col in range(len(grid[0])):
        col_map = dict()
        for row in range(len(grid)):
            if grid[row][col] in col_map.keys():
                return False
            else:
                if grid[row][col] != ".":
                    col_map[grid[row][col]] = 1
    # check 3*3
    for row in range(0, 9, 3):
      for col in range(0, 9, 3):
        if not check_small_grid(grid, row, col):
          valid = False
          return False
    return True

def check_small_grid(grid, row, col):
    small_grid_map = dict()
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if grid[i][j] != "." and grid[i][j] in small_grid_map.keys():
                return False
            else:
                small_grid_map[grid[i][j]] = 1
    return True
