f = open("sample/input1.txt", "r+")
lines = list()
for line in f:
    lines.append(line.rstrip())
f.close()

num_words = int(lines[0])
words = lines[1:]

def magic_words(words):
    magic = set()
    vowels = ("a", "e", "i", "o", "u", "y")
    for w in words:
        if 5 <= len(w) <= 7:
            if ord(w[0])+1 == ord(w[1]):
                if w[-1] in vowels:
                    magic.add(w)
    return len(magic)

print(magic_words(words))
