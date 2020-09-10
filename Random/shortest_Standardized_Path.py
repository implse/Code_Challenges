# Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.

# For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".

def shortestPath(path):
    stack = list()
    path = path.split("/")

    for segment in path:
        if segment == ".":
            continue
        elif segment == "..":
            if len(stack) > 1:
                stack.pop()
        else:
            stack.append(segment)
    return "/".join(stack)

# Test
p = "/user/bin/../bin/./scripts/../"
print(shortestPath(p))
