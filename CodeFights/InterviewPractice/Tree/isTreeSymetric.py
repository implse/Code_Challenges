# https://codefights.com/interview-practice/task/tXN6wQsTknDT6bNrf

# Given a binary tree t, determine whether it is symmetric around its center, i.e. each side mirrors the other.

# You want two pointers to go down the tree recursively, one for the left side and one for the right.
# When doing the comparison, compare the values of the left children on one side to the right children on the other, and vice-versa.

# Definition for binary tree:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

def isTreeSymmetric(t):
    def checkSymetric(sub_1, sub_2):
        if sub_1 == None and sub_2 == None:
            return True
        elif sub_1 and sub_2:
            if sub_1.value == sub_2.value and checkSymetric(sub_1.left, sub_2.right) and checkSymetric(sub_1.right, sub_2.left):
                return True
        return False
    return not t or checkSymetric(t.left, t.right)
