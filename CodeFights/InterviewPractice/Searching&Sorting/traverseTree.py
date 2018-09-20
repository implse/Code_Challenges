# Given a binary tree of integers t, return its node values in the following format:

# The first element should be the value of the tree root;
# The next elements should be the values of the nodes at height 1 (i.e. the root children), ordered from the leftmost to the rightmost one;
# The elements after that should be the values of the nodes at height 2 (i.e. the children of the nodes at height 1) ordered in the same way;
# Etc.

class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

def traverseTree(t):
    q = list()
    node_values = list()
    if t is None:
        return node_values
    q.append(t)
    while q:
        node = q.pop(0)
        node_values.append(node.value)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return node_values
