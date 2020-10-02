# Given a Binary Tree, determine if it is a valid Binary Search Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_valid_BST(root):
    def helper(node, lower, upper):
        if not node:
            return True
        value = node.value
        if value <= lower or value >= upper:
            return False
        if not helper(node.right, value, upper):
            return False
        if not helper(node.left, lower, value):
            return False
        return True
    return helper(root, float('-inf'), float('inf'))

# Test 1 : valid BST
tree_1 = Node(5)
tree_1.left = Node(1)
tree_1.right = Node(7)
tree_1.right.left = Node(6)
tree_1.right.right = Node(8)

# Test 2 : unvalid BST
tree_2 = Node(5)
tree_2.left = Node(1)
tree_2.right = Node(6)
tree_2.right.left = Node(4)
tree_2.right.right = Node(7)


print(is_valid_BST(tree_1))
print(is_valid_BST(tree_2))
