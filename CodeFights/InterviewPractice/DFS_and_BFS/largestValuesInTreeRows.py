class Node(object):
   def __init__(self, x):
     self.value = x
    self.left = None
    self.right = None

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
