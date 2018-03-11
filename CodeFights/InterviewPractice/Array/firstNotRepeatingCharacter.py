# https://codefights.com/interview-practice/task/uX5iLwhc6L5ckSyNC

# Given a string s, find and return the first instance of a non-repeating character in it.
# If there is no such character, return '_'.

def firstNotRepeatingCharacter(s):
    alphabet = {}
    for a in s:
        if a not in alphabet:
            alphabet[a] = 1
        else:
            alphabet[a] += 1
    for k in s:
        if alphabet[k] == 1:
            return k
    return "_"
