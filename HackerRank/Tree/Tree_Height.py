# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

# The height of a binary tree is the number of edges between the tree's root and its furthest leaf.
# This means that a tree containing a single node has a height of 0.

# if root == None return -1

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root == None:
        return -1
    left = height(root.left)
    right = height(root.right)
    return max(left + 1, right + 1)
