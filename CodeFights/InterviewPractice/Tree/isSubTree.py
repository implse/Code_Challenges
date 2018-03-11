# https://codefights.com/interview-practice/task/mDpAJnDQkJqaYYsCg

# Given two binary trees t1 and t2, determine whether the second tree is a subtree
# of the first tree. A subtree for vertex v in a binary tree t is a tree consisting
# of v and all its descendants in t. Determine whether or not there is a vertex v
# (possibly none) in tree t1 such that a subtree for vertex v (possibly empty) in t1 equals t2.

# Clues

# Write a separate isEqual function for comparing whether two trees are identical.
# Then, for each node v in the tree t1, check if isEqual(v, t2). You can use depth-first search for this.

class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

def isSubtree(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None:
        return False
    if t2 is None:
        return True
    if isEqual(t1, t2):
        return True
    return isSubtree(t1.left, t2) or isSubtree(t1.right, t2)

def isEqual(v1, v2):
    if v1 is None and v2 is None:
        return True
    if v1 is not None and v2 is not None:
        return (v1.value == v2.value and isEqual(v1.left, v2.left) and isEqual(v1.right, v2.right))
    return False
