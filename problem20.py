# Given two singly linked lists that intersect at some point,
# find the intersecting node. The lists are non-cyclical.
#
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
# return the node with value 8.
#
# In this example, assume nodes with the same value are the exact same node objects.
#
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        self.visited = False


class SingleLinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
        else:
            if self.tail is None:
                self.head.next = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
        return self

    def addNode(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            if self.tail is None:
                self.head.next = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
        return self

# def find_intersection(lista, listb):
#     curr_lista_node = lista.head
#     curr_listb_node = listb.head
#     while curr_lista_node:
#         while curr_listb_node:
#             if curr_lista_node.val == curr_listb_node.val:
#                 return curr_lista_node
#             curr_listb_node = curr_listb_node.next
#         curr_lista_node = curr_lista_node.next
#         curr_listb_node = listb.head


def find_intersection_with_visited(lista, listb):
    curr_lista_node = lista.head
    while curr_lista_node:
        curr_lista_node.visited = True
        curr_lista_node = curr_lista_node.next
    curr_listb_node = listb.head
    while curr_listb_node:
        if curr_listb_node.visited:
            return curr_listb_node
        curr_listb_node = curr_listb_node.next
    return None



if __name__ == "__main__":
    three = Node(3)
    seven = Node(7)
    eight = Node(8)
    ten = Node(10)
    ninenine = Node(99)
    one = Node(1)
    # lista = SingleLinkedList().add(3).add(7).add(8).add(10)
    # listb = SingleLinkedList().add(99).add(1).add(8).add(10)
    # print(find_intersection(lista, listb).val)
    lista = SingleLinkedList().addNode(three).addNode(seven).addNode(eight).addNode(ten)
    listb = SingleLinkedList().addNode(ninenine).addNode(one).addNode(eight).addNode(ten)
    print(find_intersection_with_visited(lista, listb).val)
