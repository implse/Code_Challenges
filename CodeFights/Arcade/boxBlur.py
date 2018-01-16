# https://codefights.com/arcade/intro/level-5/5xPitc3yT3dqS7XkP

# Last night you partied a little too hard. Now there's a black and white photo of you that's
# about to go viral! You can't let this ruin your reputation, so you want to apply the box blur
# algorithm to the photo to hide its content.

# The pixels in the input image are represented as integers.

# The algorithm distorts the input image in the following way: Every pixel x in the output
# image has a value equal to the average value of the pixel values from the 3 × 3 square that
# has its center at x, including x itself. All the pixels on the border of x are then removed.

# Return the blurred image as an integer, with the fractions rounded down.

def boxBlur(image):
    row = len(image)
    col = len(image[0])
    m = []
    offset_r = 0
    while offset_r + 3 <= row:
        s = []
        offset_c = 0
        while offset_c + 3 <= col:
            sum = 0
            for r in range(offset_r,3 + offset_r):
                for c in range(offset_c,3 + offset_c):
                    sum += image[r][c]
            s.append(sum//9)
            offset_c += 1
        m.append(s)
        offset_r += 1
    return m
