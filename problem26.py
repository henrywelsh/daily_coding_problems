# Given a singly linked list and an integer k, remove the kth last element from the list.
# k is guaranteed to be smaller than the length of the list.
#
# The list is very long, so making more than one pass is prohibitively expensive.
#
# Do this in constant space and in one pass.

class Node:

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class SingleLinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def append_element(self, e):
        new_node = Node(e)
        if self.head is None:
            self.head = new_node
        else:
            if self.tail is None:
                self.head.next_node = new_node
                self.tail = new_node
            else:
                self.tail.next_node = new_node
                self.tail = new_node

    def remove_nth_element(self, n):
        curr_node = self.head
        prev_node = self.head
        if n == 1:
            self.head = self.head.next_node
        else:
            curr_node = self.head.next_node
            n -= 1
            while n > 1:
                prev_node = curr_node
                curr_node = prev_node.next_node
                n -= 1
        prev_node.next_node = curr_node.next_node


if __name__ == "__main__":
    linked_list = SingleLinkedList()
    linked_list.append_element(1)
    linked_list.append_element(2)
    linked_list.append_element(3)
    linked_list.remove_nth_element(3)
