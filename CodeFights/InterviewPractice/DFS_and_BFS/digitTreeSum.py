# Given a binary tree t, find the sum of all the numbers encoded in it.

# We're going to store numbers in a tree.
# Each node in this tree will store a single digit (from 0 to 9), and each path
# from root to leaf encodes a non-negative integer.

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def digitTreeSum(t):
    all_paths = list()
    stack = list()
    find_paths_dfs(t, stack, all_paths)
    return sum(all_paths)

def find_paths_dfs(node, stack, all_paths):
  if node == None:
    return
  stack.append(node)
  find_paths_dfs(node.left, stack, all_paths)

  if node.left == None and node.right == None:
    path = [n.value for n in stack]
    num = int("".join(str(n) for n in path))
    all_paths.append(num)

  find_paths_dfs(node.right, stack, all_paths)
  stack.pop()

# Test
t = Node(1)
t.left = Node(0)
t.left.left = Node(3)
t.left.right = Node(1)
t.right = Node(4)

print(digitTreeSum(t))
