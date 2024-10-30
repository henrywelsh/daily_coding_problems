# Given the root of a binary tree, return the deepest node. For example, in the following tree, return d.
#
#     a
#    / \
#   b   c
#  /
# d


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_deepest_node(node):
    if node.left is None and node.right is None:
        return node.val
    elif node.left is None and node.right is not None:
        return find_deepest_node(node.right)
    elif node.right is not None and node.left is None:
        return find_deepest_node(node.left)