# https://app.codesignal.com/challenge/JhtBKjkeDwaaERovM

def greedyDecoding(message):
    decode = list()
    ln = len(message)
    n = 0
    while n < ln:
        one = int(message[n])
        if n < ln - 1:
            two = int(message[n]) * 10 + int(message[n + 1])
            if two <= 26:
                decode.append(chr(two + 64))
                n += 1
            else:
                decode.append(chr(one + 64))
        elif n == ln - 1:
            decode.append(chr(one + 64))
        n += 1
    return "".join(decode)

# Test
message = "195318520"
print(greedyDecoding(message))
