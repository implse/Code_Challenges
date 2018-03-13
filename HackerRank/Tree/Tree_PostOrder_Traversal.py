# https://www.hackerrank.com/challenges/tree-postorder-traversal/problem

# Complete the postOrder function in your editor below, which has  parameter: a pointer to the root of a binary tree.
# It must print the values in the tree's postorder traversal as a single line of space-separated values.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postOrder(root):
    result = []
    def traverse(node):
        if node.left:
            traverse(node.left)
        if node.right:
            traverse(node.right)
        result.append(node.data)
    traverse(root)
    print(" ".join(str(i) for i in result))
