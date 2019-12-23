# Test Select
number = "1"

# Read Input (line by line)
lines = list()
f = open("sample/input"+ number + ".txt", "r+")
n = f.read()
f.close()
lines = n.split("\n")
print(lines)

# Read Output
output = list()
f = open("sample/output" + number + ".txt", "r+")
n = f.read()
f.close()
output = n.split("\n")
print(output)

def check_palindrome(w):
    i = 0
    j = len(w) - 1
    while i < j:
        if w[i] != w[j]:
            return False
        i += 1
        j -= 1
    return True
n = int(lines[0])
palindrome = list()
for i in range(1, n + 1):
    word = lines[i]
    if check_palindrome(word):
        palindrome.append(word)
print(" ".join(palindrome))
