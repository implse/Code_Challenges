# Given an url where the character are in reverse order write a function to return the correct url.

# sptth://www.doolf.moc.retneprac return https://www.flood.com/carpenter

reverse = "sptth://www.doolf.moc.retneprac"

# Time O(n) / Space O(n)
def un_reverse(url):
    stack = list()
    output_url = ""
    for char in url:
        if char not in [":", "/", "."]:
            stack.append(char)
        else:
            while len(stack) > 0:
                output_url += stack.pop()
            output_url += char
    if len(stack) > 0:
        output_url += "".join(stack)[::-1]
    return output_url

print(un_reverse(reverse))

