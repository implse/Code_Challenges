# https://codefights.com/arcade/intro/level-3/3o6QFqgYSontKsyk4

# You have a string s that consists of English letters, punctuation marks,
# whitespace characters, and brackets.
# It is guaranteed that the parentheses in s form a regular bracket sequence.

# Your task is to reverse the strings contained in each pair of matching parentheses,
# starting from the innermost pair. The results string should not contain any parentheses.

import re

def reverseParentheses(s):
    while "(" in s:
        return reverseParentheses(regex_rev(s))
    return s

def regex_rev(s):
    rgx = "\([^()]*\)"
    match = re.search(rgx, s)
    w = match.group(0)[::-1]
    return s.replace(match.group(0), w[1:-1])

# test 1
s = "a(bc)de"
# test 2
s ="a(bcdefghijkl(mno)p)q"


print(reverseParentheses(s))
# print(regex_rev(s))
