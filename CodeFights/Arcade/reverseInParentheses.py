def reverseInParentheses(inputString):
    ln_str = len(inputString)
    output_stack = []
    for i in range(ln_str):
        if inputString[i] != ")":
            output_stack.append(inputString[i])
        else:
            close_stack = []
            while output_stack[-1] != "(":
                close_stack.append(output_stack.pop())
            dustbin = output_stack.pop()

            output_stack += close_stack
    return "".join(output_stack)

# Test
str = "foo(bar(baz))blim" # foobazrabblim

print(reverseInParentheses(str))
