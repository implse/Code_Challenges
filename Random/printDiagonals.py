# Given a 2D list print all diagonal from left to right and from right to left

board = [
    [1, 3, 6, 10, 15, 21],
    [2, 4, 9, 14, 20, 26],
    [4, 8, 13, 19, 25, 30],
    [7, 12, 18, 24, 29, 33],
    [11, 17, 23, 28, 32, 35],
    [16, 22, 27, 31, 34, 36]
]

def diagonals(board):
    ln = len(board)
    # diagonal top left bottom right
    for row in range(ln):
        diag_row = row
        diag_col = 0
        while diag_row < ln:
            print(board[diag_row][diag_col], end= " ")
            diag_row += 1
            diag_col += 1
        print()
    for col in range(1, ln):
        diag_row = 0
        diag_col = col
        while diag_col < ln:
            print(board[diag_row][diag_col], end= " ")
            diag_row += 1
            diag_col += 1
        print()

print(diagonals(board))
