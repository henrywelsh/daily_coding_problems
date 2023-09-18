# Implement an autocomplete system.
# That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.
#
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
#
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

def find_all_prefixed_strings(prefix, string_list):
    return [n for n in string_list if n[0:len(prefix)] == prefix]


class TreeString:
    # val corresponds to the character representation at this node
    # terminating_strings are all strings which end here or would end in a subnode
    # next_chars are all the possible next characters with strings associated
    def __init__(self, val=None, terminating_strings=None, next_chars=None):
        if next_chars is None:
            next_chars = dict()
        if terminating_strings is None:
            terminating_strings = list()
        self.val = val
        self.terminating_strings = terminating_strings
        self.next_chars = next_chars

    def add(self, n, depth):
        curr_node = self
        k = 0
        while k < depth:
            curr_char = n[k]
            if curr_char not in curr_node.next_chars:
                curr_node.next_chars[curr_char] = TreeString(curr_char, None, None)
                curr_node = curr_node.next_chars[curr_char]
            else:
                curr_node = curr_node.next_chars[curr_char]
            k += 1
        curr_node.terminating_strings.append(n)


def build_string_tree(depth, string_list):
    root_node = TreeString()
    for n in string_list:
        root_node.add(n, depth)
    return root_node



if __name__ == "__main__":

    tree_mapping = build_string_tree(2, ["dog", "deer", "deal"])
    for i in "de":
        tree_mapping = tree_mapping.next_chars.get(i)
    print(tree_mapping.terminating_strings)

