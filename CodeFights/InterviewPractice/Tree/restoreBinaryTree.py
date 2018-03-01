# https://codefights.com/interview-practice/task/AaWaYxi8gjtbqgp2M

# Given the inorder and preorder traversals of a binary tree t, but not t itself, restore t and return it.

# Clues

# The first item in preorder is the root of the tree.
# All elements to the left of the root in the list inorder are on the left side
# of the tree, while each element on the right side of root in the list inorder are on the right side of the tree

# Once the root is extracted, and the problem has been split into left and right sides,
# you can split the lists inorder and preorder into the appropriate lists for left and right trees.
# Then use recursion to restore the left and right subtrees of the root.

class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def restoreBinaryTree(inorder, preorder):
    if not inorder or not preorder:
        return None
    root = Tree(preorder[0])
    left_length = inorder.index(preorder[0])
    root.left = restoreBinaryTree(inorder[:left_length], preorder[1:left_length+1])
    root.right = restoreBinaryTree(inorder[left_length+1:], preorder[left_length+1:])
    return root
