# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.
#
# For example, given the following Node class
#
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'


# Take this object Node('root', Node('left', Node('left.left')), Node('right')) and turn it into
# "Node(val: root,
#   Left: Node(val: left,
#       Left: Node(val: left.left, Left: None, Right: None), Right: None),
#   Right: Node(val: right, Left: None, Right: None))
def serialize(root):
    if root is None:
        return "None"
    node_string_rep = str()
    node_string_rep += ("Node(val: " + str(root.val) + ", ")
    if root.left is None:
        node_string_rep += "left: None"
    else:
        node_string_rep += ("left: " + str(serialize(root.left)))
    if root.right is None:
        node_string_rep += ", right: None)"
    else:
        node_string_rep += (", right: " + str(serialize(root.right)) + ")")
    return node_string_rep


def deserialize(root):
    if root == "None":
        return None
    else:
        root = root[5:]
        root = root[:-1]
        split_root = split_string(root)
        return Node(split_root[0].split(":")[1].strip(), deserialize(split_root[1][5:].strip()), deserialize(split_root[2][6:].strip()))


def split_string(node_string):
    res_split = []
    curr_string = str()
    count_paren = 0
    for c in node_string:
        if c == '(':
            count_paren += 1
            curr_string += c
        elif c == ')':
            count_paren -= 1
            curr_string += c
        elif c == ',' and count_paren == 0:
            res_split.append(curr_string.strip())
            curr_string = str()
            count_paren = 0
        else:
            curr_string += c
    if len(curr_string) > 0:
        res_split.append(curr_string.strip())
    return res_split


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(serialize(node))
    print(deserialize(serialize(node)).left.left.val)
