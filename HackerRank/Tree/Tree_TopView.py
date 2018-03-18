# https://www.hackerrank.com/challenges/tree-top-view/problem

# You are given a pointer to the root of a binary tree. Print the top view of the binary tree.
# Top view means when you look the tree from the top the nodes you will see will be called the top view of the tree.

# Python 2.7 print
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def go_left(node):
    if node.left != None:
        go_left(node.left)
    print node.data,

def go_right(node):
    print node.data,
    if node.right != None:
        go_right(node.right)

def topView(root):
    if root.left != None:
        go_left(root.left)
    print root.data,
    if root.right != None:
        go_right(root.right)
