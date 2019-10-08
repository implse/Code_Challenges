# https://codefights.com/interview-practice/task/uX5iLwhc6L5ckSyNC

# Given a string s, find and return the first instance of a non-repeating character in it.
# If there is no such character, return '_'.

# Better solution : time O(n) / space O(1)
def firstNotRepeatingCharacter(s):
    alphabet = [[0, 0] for _ in range(26)]
    for i in range(len(s)):
        char_code = ord(s[i]) - 97
        alphabet[char_code][0] += 1     
        alphabet[char_code][1] = i
    index = float("inf")
    for char in alphabet:
        if char[0] == 1:
            index = min(index, char[1])
    return s[index] if index < float("inf") else "_"

    
# Naïve Solution : time O(n^2) / space O(n)
def firstNotRepeatingCharacter__(s):
    alphabet = {}
    for char in s:
        alphabet[char] = 1 if char not in alphabet else alphabet[char]+1     
    for char in s:
        if alphabet[char] == 1:
            return char
    return "_"
