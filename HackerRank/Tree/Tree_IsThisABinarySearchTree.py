# https://www.hackerrank.com/challenges/is-binary-search-tree/problem

# InOrder:
#     - Traverse the left sub tree.
#     - Visit the root
#     - Travrse the right sub tree.


class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

inOrder_value = []

def inOrder(root):
    current = root
    if current == None:
        return None
    else:
        if current.left:
            inOrder(current.left)
        inOrder_value.append(current.data)
        if current.right:
            inOrder(current.right)

def check_binary_search_tree_(root):
    inOrder(root)
    a = inOrder_value[0]
    for i in range(1, len(inOrder_value)):
        b = inOrder_value[i]
        if a >= b:
            return False
        a = b
    return True
