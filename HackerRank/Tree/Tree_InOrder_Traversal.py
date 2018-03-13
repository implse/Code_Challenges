# https://www.hackerrank.com/challenges/tree-preorder-traversal/problem

# Complete the preOrder function in your editor below, which has  parameter:
# a pointer to the root of a binary tree.
# It must print the values in the tree's preorder traversal as a single line of space-separated values.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):
    result = []
    def traverse(node):
        if node.left:
            traverse(node.left)
        result.append(node.data)
        if node.right:
            traverse(node.right)
    traverse(root)
    print(" ".join(str(i) for i in result))
