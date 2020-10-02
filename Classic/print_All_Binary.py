# Write a recursive function that accepts an integer number of digits and prints 
# all binary numbers that have exactly that many digits, in ascending order, one per line.


def print_all_binary(n):
    def print_all_binary_helper(n, output):
        if n == 0:
            print(output)
        else:
            print_all_binary_helper(n - 1, output + "0")
            print_all_binary_helper(n - 1, output + "1")
    return print_all_binary_helper(n, "")


print_all_binary(3)
