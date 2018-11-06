# You have a binary tree t. Your task is to find the largest value in each row of this tree.
# In a tree, a row is a set of nodes that have equal depth.
# For example, a row with depth 0 is a tree root, a row with depth 1 is composed of the root's children, etc.

# Return an array in which the first element is the largest value in the row with depth 0,
# the second element is the largest value in the row with depth 1, the third element is the
# largest element in the row with depth 2, etc

class Node(object):
   def __init__(self, x):
     self.value = x
    self.left = None
    self.right = None

# Recursive Solution
def largestValuesInTreeRows(t):
    max_list = list()
    largestHelper(max_list, t, 0)
    return max_list

def largestHelper(max_list, node, d):
    if node == None:
        return
    if d == len(max_list):
        max_list.append(node.value)
    else:
        max_list[d] = max(node.value, max_list[d])

    largestHelper(max_list, node.left, d + 1)
    largestHelper(max_list, node.right, d + 1)

# Iterative Solution
import math
def largestValuesInTreeRows(t):
    max_list = list()
    queue = list()
    queue.append(t)
    maximum = math.inf * - 1
    if t == None:
        return max_list
    while true:
        node_count = len(queue)
        if node_count == 0:
            break
        while nc - 1 > 0:
            n = queue.pop(0)
            maximum = max(maximum, n.value)
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
        max_list.append(maximum)
    return max_list
