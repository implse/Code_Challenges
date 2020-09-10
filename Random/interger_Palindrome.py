# Write a program that checks whether an integer is a palindrome.
# For example, 121 is a palindrome, as well as 888. 678 is not a palindrome.
# Do not convert the integer into a string.

def num_palindrome(num):
    n = num
    reversed_num = 0
    while n != 0:
        reversed_num = (reversed_num * 10) + (n % 10)
        n = n // 10
    return num == reversed_num
