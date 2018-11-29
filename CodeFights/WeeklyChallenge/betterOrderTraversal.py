# https://app.codesignal.com/challenge/W3nmGcuKzkg9AeEwo

# Given a binary tree, your task is to test each of these traversals,
# store the values in an array (in the order in which they're visited),
# and return the one that's lexicographically smallest.

def betterOrderTraversal(root):
    pre_order = list()
    in_order = list()
    post_order = list()

    def in_order_dfs(tree):
        if not tree:
            return
        if tree.left:
            in_order_dfs(tree.left)
        in_order.append(tree.value)
        if tree.right:
            in_order_dfs(tree.right)

    def pre_order_dfs(tree):
        if not tree:
            return
        pre_order.append(tree.value)
        if tree.left:
            pre_order_dfs(tree.left)
        if tree.right:
            pre_order_dfs(tree.right)

    def post_order_dfs(tree):
        if not tree:
            return
        if tree.left:
            post_order_dfs(tree.left)
        if tree.right:
            post_order_dfs(tree.right)
        post_order.append(tree.value)

    in_order_dfs(root)
    pre_order_dfs(root)
    post_order_dfs(root)

    lexicographically_smallest = [in_order, pre_order, post_order]
    lexicographically_smallest.sort()

    return lexicographically_smallest[0]
