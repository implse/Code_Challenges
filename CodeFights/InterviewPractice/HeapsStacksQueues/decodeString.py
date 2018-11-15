# Given an encoded string, return its corresponding decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square
# brackets is repeated exactly k times. Note: k is guaranteed to be a positive integer.



def decodeString(s):
    nStack = list()
    wStack = [""]
    num = 0
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        else:
            if c == "[":
                nStack.append(num)
                num = 0
                wStack.append("")
            elif c == "]":
                coef = nStack.pop()
                word = wStack.pop()
                print(wStack)
                wStack[len(wStack)-1] += word * coef
            else:
                wStack[len(wStack)-1] += c
    return wStack.pop()
