# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.
#
# For example, the following tree has 5 unival subtrees:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class TreeNode:
    def __init__(self, val, leftChild=None, rightChild=None):
        self.val = val
        self.leftChild = leftChild
        self.rightChild = rightChild


def find_unival_trees(node):
    if node is None:
        return 0, True
    if node.leftChild is None and node.rightChild is None:
        return 1, True
    left_child_unival = find_unival_trees(node.leftChild)
    right_child_unival = find_unival_trees(node.rightChild)
    if ((left_child_unival[1] is True and right_child_unival[1] is True)
            and (node.leftChild is None or node.leftChild.val == node.val)
            and (node.rightChild is None or node.rightChild.val == node.val)):
        return (left_child_unival[0] + right_child_unival[0] + 1), True
    else:
        return (left_child_unival[0] + right_child_unival[0]), False


if __name__ == "__main__":
    rootNode = TreeNode(0,
                        TreeNode(1),
                        TreeNode(0,
                                 TreeNode(1,
                                          TreeNode(1),
                                          TreeNode(1)),
                                 TreeNode(0)))
    print(find_unival_trees(rootNode)[0])
    fiveNode = TreeNode(5, TreeNode(5, TreeNode(5), TreeNode(5)), TreeNode(5, None, TreeNode(5)))
    print(find_unival_trees(fiveNode)[0])