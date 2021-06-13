# Given a grid of size n * m remove all 1 that are not connected to the border of the grid.
# A cell is connected to its adjacent cells in this direction : top, bottom, left and right only.


# DFS returning a list of connected cells
def dfs(grid, row, col):
    ln_row = len(grid)
    ln_col = len(grid[0])
    stack = [(row, col)]
    visited = [[False for i in range(ln_col)] for j in range(ln_row)]
    connected = []
    while len(stack) > 0:
        c_row, c_col = stack.pop()
        neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for n in neighbours:
            n_row = c_row + n[0]
            n_col = c_col + n[1]
            if n_row >= 0 and n_row < ln_row and n_col >= 0 and n_col < ln_col and grid[n_row][n_col] == 1:
                if visited[n_row][n_col] == False:
                    stack.append((n_row, n_col))
                    visited[n_row][n_col] = True
                    connected.append((n_row, n_col))
    return connected

# Remove Islands : In place grid modifications
def removeIslands(grid):
    ln_row = len(grid)
    ln_col = len(grid[0])
    removable = [[True for i in range(ln_col)] for j in range(ln_row)]
    not_removable = []

    # Iterate over grid border
    for i in range(ln_col):
        if grid[0][i] == 1:
            not_removable.append((0, i))
            c = dfs(grid, 0, i)
            if len(c) > 0:
                not_removable += c
        if grid[ln_row - 1][i] == 1:
            not_removable.append((ln_row - 1, i))
            c = dfs(grid, ln_row - 1, i)
            if len(c) > 0:
                not_removable += c

    # Iterate over grid border
    for j in range(ln_row):
        if grid[j][0] == 1:
            not_removable.append((j, 0))
            c = dfs(grid, j, 0)
            if len(c) > 0:
                not_removable += c
        if grid[j][ln_col - 1] == 1:
            not_removable.append((j, ln_col - 1))
            c = dfs(grid, j, ln_col - 1)
            if len(c) > 0:
                not_removable += c

    # Fill not_removeable grid if current cell is not removable
    if len(not_removable) > 0:
        for nr in not_removable:
            r_row, r_col = nr
            removable[r_row][r_col] = False

    # Remove removable cells if the cell is equal to 1
    for r in range(ln_row):
        for c in range(ln_col):
            if removable[r][c] == True and grid[r][c] == 1:
                grid[r][c] = 0

# Test

grid = [
    [1, 0, 0, 0, 0, 0,],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

# Helper print grid
def print_grid(grid):
    for row in grid:
        print(row)

print_grid(grid)

print("- - - - - - - - -")

removeIslands(grid)

print_grid(grid)
