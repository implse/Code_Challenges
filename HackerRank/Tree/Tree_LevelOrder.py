# https://www.hackerrank.com/challenges/tree-level-order-traversal/problem

# You are given a pointer to the root of a binary tree.
# You need to print the level order traversal of this tree.
# In level order traversal, we visit the nodes level by level from left to right.


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelOrder(root):
    if root == None:
        return
    q = []
    level = []
    current = root
    q.append(current)
    while len(q) > 0:
        current = q.pop(0)
        level.append(current.data)
        if current.left != None:
            q.append(current.left)
        if current.right != None:
            q.append(current.right)
    print(" ".join(str(i) for i in level))
