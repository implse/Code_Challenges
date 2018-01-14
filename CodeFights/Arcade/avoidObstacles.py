# https://codefights.com/arcade/intro/level-5/XC9Q2DhRRKQrfLhb5/description

# You are given an array of integers representing coordinates of obstacles situated on a straight line.

# Assume that you are jumping from the point with coordinate 0 to the right.
# You are allowed only to make jumps of the same length represented by some integer.

# Find the minimal length of the jump enough to avoid all the obstacles.

def avoidObstacles(inputArray):
    inputArray.sort()
    last = inputArray[-1]
    for step in range(2, last+2):
        jump = 0
        while last > jump:
            notFail = True
            jump += step
            if jump in inputArray:
                notFail = False
                break
        if notFail:
            return step        
