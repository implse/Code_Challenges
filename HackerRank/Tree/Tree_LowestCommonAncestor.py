# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem

# You are given pointer to the root of the binary search tree and two values v1 and v2.
# You need to return the lowest common ancestor (LCA) of  and  in the binary search treeself.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Recursive Solution
def lca(root, v1, v2):
    current = root
    if current.data > max(v1, v2):
        return lca(current.left, v1, v2)
    elif current.data < min(v1, v2):
        return lca(current.right, v1, v2)
    else:
        return current
