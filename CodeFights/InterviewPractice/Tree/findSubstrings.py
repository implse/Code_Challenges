# https://codefights.com/interview-practice/task/Ki9zRh5bfRhH6oBau/description

# You have two arrays of strings, words and parts.
# Return an array that contains the strings from words, modified so that any occurrences
# of the substrings from parts are surrounded by square brackets [], following these guidelines:

# If several parts substrings occur in one string in words, choose the longest one.
# If there is still more than one such part, then choose the one that appears first in the string.

class Node(object):
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.endOfWord = False

def addFragment(root, fragment):
    current = root
    for l in fragment:
        if l not in current.children:
            current.children[l] = Node(l)
        current = current.children[l]
    current.endOfWord = True

def findSubstringInWord(w, root):
    lnLongSubstr = 0
    longestPos = 0
    ln = len(w)
    for start_pos in range(ln):
        current = root
        for position in range(start_pos, ln):
            l = w[position]
            if l not in current.children:
                break
            current = current.children[l]
            length = position - start_pos + 1
            if current.endOfWord and length > lnLongSubstr:
                lnLongSubstr = length
                longestPos = start_pos
    if lnLongSubstr == 0:
        return w
    end = longestPos + lnLongSubstr
    return w[:longestPos] + "[" + w[longestPos: end] + "]" + w[end:]

def findSubstrings(words, parts):
    root = Node("*")
    for p in parts:
        addFragment(root, p)
    return [findSubstringInWord(w, root) for w in words]
