
class Node:
    def __init__(self, x=None, next_node=None):
        self.val = x
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = Node()

    def insert(self, x):
        self.head.next = Node(x, self.head.next)

    def search(self, key):

        ptr = self.head

        while ptr.next:
            if ptr.val == key:
                return ptr
            ptr = ptr.next

        return None

    def delete_node(self, key):
        pass
