from src.linkedlist import LinkedList
from src.node import Node

from random import *


def linked_list_helper(num_nodes=5):
    nodes = [Node(randint(1, 1000)) for _ in range(num_nodes)]
    test_ll = LinkedList()

    for node in nodes:
        test_ll.insert_tail(node)

    return test_ll, nodes


class TestLinkedList(object):

    def test_insert_tail(self):
        test_ll, nodes = linked_list_helper(5)
        new_node = Node(5)
        test_ll.insert_tail(new_node)
        tail_node = test_ll.get_tail()
        assert tail_node.data == 5

    def test_get_tail(self):
        test_ll, nodes = linked_list_helper(5)
        tail_node = test_ll.get_tail()
        assert tail_node == nodes[4]

    def test_is_empty(self):
        test_ll, nodes = linked_list_helper()
        assert test_ll.is_empty() == False

    def test_traversal(self):
        test_ll, nodes = linked_list_helper()

        for test_node, list_node in zip(test_ll.interate(), nodes):
            if test_node.data != list_node.data:
                assert False
        assert True

    def test_size(self):
        test_ll, nodes = linked_list_helper()
        assert test_ll.is_empty() == False

    def test_get_head(self):
        test_ll, nodes = linked_list_helper()
        assert test_ll.get_head() is nodes[0]

    def test_insert_head(self):
        test_ll, nodes = linked_list_helper()
        assert test_ll.get_head() is nodes[0]

    def test_has_data(self):
        test_ll, nodes = linked_list_helper()
        test_data = nodes[3].data
        assert test_ll.has_data(test_data) == True

    def test_remove_specific(self):
        test_ll, nodes = linked_list_helper(5)

        test_data = nodes[3].data

        test_ll.remove_data(test_data)

        assert test_ll.has_data(test_data) == False

    def test_remove_tail(self):
        test_ll, nodes = linked_list_helper(5)
        test_ll.remove_tail()
        assert test_ll.get_tail().data != nodes[4].data

    def test_remove_head(self):
        test_ll, nodes = linked_list_helper()
        test_ll.remove_head()
        assert test_ll.get_head().data != nodes[0].data
