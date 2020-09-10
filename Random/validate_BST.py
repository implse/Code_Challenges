# Validate a BST

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Valid BST
tree_1 = Node(5)
tree_1.left = Node(3)
tree_1.left.left = Node(2)
tree_1.left.left.left = Node(1)
tree_1.left.right = Node(4)
tree_1.right = Node(7)
tree_1.right.left = Node(6)
tree_1.right.right = Node(8)
tree_1.right.right.right = Node(9)

# Not Valid BST
tree_2 = Node(5)
tree_2.left = Node(4)
tree_2.left.right = Node(3)
tree_2.left.left = Node(2)
tree_2.left.left.left = Node(1)
tree_2.right = Node(9)
tree_2.right.left = Node(8)
tree_2.right.left.right = Node(6)
tree_2.right.left.right = Node(5)


# Helper method
def isValidHelper(node, low, high):
    if node == None:
        return True
    if node.value > low and node.value < high and isValidHelper(node.left, low, node.value) and isValidHelper(node.right, node.value, high):
        return True
    return False

# Valid method
def isValid(node):
    return isValidHelper(node, float("-inf"), float("inf"))

print(isValid(tree_1))

print(isValid(tree_2))
