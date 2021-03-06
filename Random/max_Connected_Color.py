# Given a grid find the maximum connected color

# Main function
def connectedColor(grid):
    max_color_connected = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            max_current = bfs(grid, r, c)
        max_color_connected = max(max_color_connected, max_current)
    return max_color_connected

# Breadth First Search - return max connected
def bfs(grid, r, c):
    queue = list()
    visited = list()
    queue.append((r, c))
    visited.append((r, c))
    color = grid[r][c]
    max_color = 1

    while len(queue) > 0:
        cell = queue.pop(0)
        row, column = cell
    # check top bottom
        for i in range(row - 1, row + 2):
          if 0 <= i < len(grid) and color == grid[i][column]:
            # check already visited
            if (i, column) not in visited:
              max_color += 1
              queue.append((i, column))
              visited.append((i, column))
        # Check left right
        for j in range(column - 1, column + 2):
          if 0 <= j < len(grid[0]) and color == grid[row][j]:
            # check already visited
            if (row, j) not in visited:
              max_color += 1
              queue.append((row, j))
              visited.append((row, j))
    return max_color

# Breadth First Search - return max color connected coordinates (tuples)
def bfs_coordinates(grid, r, c):
    queue = list()
    visited = list()
    queue.append((r, c))
    visited.append((r, c))
    color = grid[r][c]
    max_color = 1
    color_grid = set()

    while len(queue) > 0:
        cell = queue.pop(0)
        row, column = cell
        # check top bottom
        for i in range(row - 1, row + 2):
          if 0 <= i < len(grid) and color == grid[i][column]:
            color_grid.add((i, column))
            if (i, column) not in visited:

              max_color += 1
              queue.append((i, column))
              visited.append((i, column))
        # Check left right
        for j in range(column - 1, column + 2):
          if 0 <= j < len(grid[0]) and color == grid[row][j]:
            color_grid.add((row, j))
            if (row, j) not in visited:
              max_color += 1
              queue.append((row, j))
              visited.append((row, j))
    return color_grid


# Test - max connected color Blue = 5
grid = [
  ["G", "G", "B", "R"],
  ["G", "B", "R", "B"],
  ["R", "B", "B", "B"]
]

print(connectedColor(grid))
print(bfs_coordinates(grid, 0, 0))
