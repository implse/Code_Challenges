# Given tree, a binary tree, your task is to determine whether or not it's a BST (return true if it is, or false if it isn't).

import math

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

min = math.inf * - 1
max = math.inf

def isBinarySearchTree_helper(node, min, max):
    if node == None:
        return True
    if node.value < min or node.value > max:
        return False
    return isBinarySearchTree_helper(node.left, min, node.value - 1) and isBinarySearchTree_helper(node.right, node.value + 1, max)

def isBinarySearchTree(tree):
    return isBinarySearchTree_helper(tree, min, max)

# Test1 - True
t1 = Node(5)
t1.left = Node(3)
t1.left.left = Node(2)
t1.right = Node(8)
t1.right.left = Node(6)
t1.right.right = Node(9)

# Test2 - False
t2 = Node(9)
t2.left = Node(8)
t2.left.left = Node(2)
t2.left.right = Node(6)
t2.right = Node(5)

def dfs_inorder(node):
    if node == None:
        return
    if node.left:
        dfs_inorder(node.left)
    print(node.value)
    if node.right:
        dfs_inorder(node.right)

dfs_inorder(t2)
print(isBinarySearchTree(t2))
