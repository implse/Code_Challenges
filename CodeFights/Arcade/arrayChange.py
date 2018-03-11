# https://codefights.com/arcade/intro/level-4/xvkRbxYkdHdHNCKjg

# You are given an array of integers. On each move you are allowed to increase exactly
# one of its element by one. Find the minimal number of moves required to obtain a
# strictly increasing sequence from the input.

def arrayChange(inputArray):
    mv = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[i - 1]:
            df = (inputArray[i - 1] + 1) - inputArray[i]
            mv += df
            inputArray[i] = inputArray[i - 1] + 1
    return mv
