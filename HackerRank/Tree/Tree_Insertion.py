# https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem

# You are given a pointer to the root of a binary search tree and a value to be inserted into the tree.
# Insert this value into its appropriate position in the binary search tree and return the root of the updated binary tree.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(r,val):
    if r == None:
        r = Node(val)
    if val < r.data:
        if r.left == None:
            r.left = Node(val)
        else:
            insert(r.left, val)
    if val > r.data:
        if r.right == None:
            r.right = Node(val)
        else:
            insert(r.right, val)
    return r

bst = Node(4)
bst.left = Node(2)
bst.left.right = Node(3)
bst.left.left = Node(1)
bst.right = Node(7)
