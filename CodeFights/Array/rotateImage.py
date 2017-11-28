# https://codefights.com/interview-practice/task/5A8jwLGcEpTPyyjTB

# You are given an n x n 2D matrix that represents an image.
# Rotate the image by 90 degrees (clockwise).

def rotateImage(a):
    row = len(a)
    col = len(a[0])
    rotate = []
    for c in range(col):
        p = []
        for r in range(row):
            p.append(a[row - 1 - r][c])
        rotate.append(p)
    return rotate
