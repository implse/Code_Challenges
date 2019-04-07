# Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.

# For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:

#     5
#    / \
#   3   7
#  / \   \
# 2   4   8

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = None
    # Insert root
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.insertNode(value, self.root)
    # Insert Node
    def insertNode(self, value, node):
        # left child
        if value < node.value:
            if node.left:
                self.insertNode(value, node.left)
            else:
                node.left = Node(value)
        # right child
        if value > node.value:
            if node.right:
                self.insertNode(value, node.right)
            else:
                node.right = Node(value)
    # DepthFirstSearch
    def DepthFirstSearch(self):
        if not self.root:
            return None
        else:
            result = []
            def DepthFirstSearch_post_order(node):
                if node.left:
                    DepthFirstSearch_post_order(node.left)
                if node.right:
                    DepthFirstSearch_post_order(node.right)
                result.append(node.value)
            DepthFirstSearch_post_order(self.root)
        return result
# Reconstruct function
def reconstruct_tree(lst):
    t = Tree()
    for n in lst[::-1]:
        t.insert(n)
    return t

# Test
lst = [2, 4, 3, 8, 7, 5]

t = reconstruct_tree(lst)
print(t.DepthFirstSearch())
