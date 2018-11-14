# A tree is considered a binary search tree (BST) if for each of its nodes the following is true:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and the right subtrees must also be binary search trees.
# Removing a value x from a BST t is done in the following way:

# If there is no x in t, nothing happens;
# Otherwise, let t' be a subtree of t such that t'.value = x.
# If t' has a left subtree, remove the rightmost node from it and put it at the root of t';
# Otherwise, remove the root of t' and its right subtree becomes the new t's root.

class Node(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def find_rightmost(node):
    if node == None:
        return None
    if node.right == None:
        return node.value
    return find_rightmost(node.right)

def isRoot(t, value):
    if t.value == value:
        return True
    return False

def removeNode(node, value):
    # search the value
    if node == None:
        return node
    elif value < node.value:
        node.left = removeNode(node.left, value)
    elif value > node.value:
        node.right = removeNode(node.right, value)
    else:
        # case 1: No child
        if node.left == None and node.right == None:
            node = None
        # case 2: One child
        elif node.left == None:
            node = node.right
        elif node.right == None:
            node = node.left
        # case 3: Two Children
        else:
            rightmost = find_rightmost(node.left)
            node.value = rightmost
            node.left = removeNode(node.left, rightmost)
    return node

def deleteFromBST(t, queries):
    for q in queries:
        removeNode(t, q)
        if isRoot(t, q):
            t.value = None
            break
    return t
