# https://codefights.com/interview-practice/task/TG4tEMPnAc3PnzRCs

# Given a binary Node t and an integer s, determine whether there is a root to leaf path
# in t such that the sum of vertex values equals s.

# Clues

# Implement a recursive solution. A node is only a leaf if BOTH its left and right children are null.

# Strategy: subtract the node value from the sum when recurring down,
#  and check to see if the sum is 0 when you run out of Node.

# Definition for binary Node:
class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def hasPathWithGivenSum(t, s):
    if t == None:
        return s == 0
    else:
        ans = False
        subSum = s - t.value
        if subSum == 0 and t.left == None and t.right == None:
            return True
        if t.left != None:
            ans = ans or hasPathWithGivenSum(t.left, subSum)
        if t.right != None:
            ans = ans or hasPathWithGivenSum(t.right, subSum)
        return ans
