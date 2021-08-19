import sys

input = sys.stdin.readline

# For taking integer inputs.
def integer_input():
    return(int(input()))

# For taking List inputs.
def list_input():
    return(list(map(int,input().split())))

# For taking string inputs. Actually it returns a List of Characters, instead of a string, which is easier to use in Python, because in Python, Strings are Immutable.
def string_input():
    s = input()
    return(list(s[:len(s) - 1]))

# For taking space seperated integer variable inputs.   
def space_integer_input():
    return list(map(int,input().split()))

