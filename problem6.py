# An XOR linked list is a more memory efficient doubly linked list.
# Instead of each node holding next and prev fields, it holds a field named both,
# which is an XOR of the next node and the previous node.
# Implement an XOR linked list; it has an add(element) which adds the element to the end,
# and a get(index) which returns the node at index.
#
# If using a language that has no pointers (such as Python),
# you can assume you have access to get_pointer and dereference_pointer
# functions that converts between nodes and memory addresses.

class Node:

    def __init__(self, val, both=0):
        self.val = val
        self.both = both


class XOR_Linked_List:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
        else:
            # Retrieve memory address of new element
            new_tail_mem_addr = get_pointer(new_node)
            # The only reference right now for the new tail is the old tail
            new_node.both = get_pointer(self.tail)
            # The old tail need the reference to the new tail memory address
            self.tail.both = self.tail.both ^ new_tail_mem_addr
            # The new tail should be the new element
            self.tail = new_node
        return self

    def get(self, index):
        current_node = None
        prev_addr = None
        if index == 0:
            return self.head
        while index > 0:
            if current_node is None:
                # If this is the first then we can just take the reference in the head node and go to it
                current_node = dereference_pointer(self.head.both)
                # Set the head as the previous address
                prev_addr = get_pointer(self.head)
            else:
                # Store the current node which will become the previous node once we move down the list
                tmp_addr = get_pointer(current_node)
                # XOR the previous address with the current address to get the address of the next node
                current_node = dereference_pointer(prev_addr ^ tmp_addr)
                # Store the previous node address
                prev_addr = tmp_addr
            index -= 1
        return current_node


