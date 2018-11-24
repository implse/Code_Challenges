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


# Breadth First Search Method
def largestValuesInTreeRows1(t):
  max_list = list()
  largestValuesInTreeRows_bfs(t, max_list)
  return max_list


def largestValuesInTreeRows_bfs(t, max_list):
  if t == None:
    return
  queue = list()
  depth = 0
  queue.append((t, depth))

  while queue:
    n, depth = queue.pop(0)
    if depth == len(max_list):
      max_list.append(n.value)
    else:
      max_list[depth] = max(max_list[depth], n.value)
    if n.left:
      queue.append((n.left, depth + 1))
    if n.right:
      queue.append((n.right, depth + 1))


# Depth First Search Method
def largestValuesInTreeRows2(t):
  max_list = list()
  largestValuesInTreeRows_dfs(t, max_list, 0)
  return max_list


def largestValuesInTreeRows_dfs(t, max_list, depth):
  if t == None:
    return
  if depth == len(max_list):
    max_list.append(t.value)
  else:
    max_list[depth] = max(max_list[depth], t.value)
  largestValuesInTreeRows_dfs(t.left, max_list, depth + 1)
  largestValuesInTreeRows_dfs(t.right, max_list, depth + 1)


# Test

t1 = Node(1)
# depth 1
t1.left = Node(2)
t1.right = Node(3)
# depth 2
t1.left.left = Node(4)
t1.left.right = Node(5)
t1.right.left = Node(6)
t1.right.right = Node(7)
# depth 3
t1.left.left.left = Node(8)
t1.left.left.right = Node(9)
t1.left.right.left = Node(10)
t1.left.right.right = Node(11)
t1.right.left.left = Node(12)
t1.right.left.right = Node(13)
t1.right.right.left = Node(14)
t1.right.right.right = Node(15)

print(largestValuesInTreeRows1(t1))
print(largestValuesInTreeRows2(t1))
