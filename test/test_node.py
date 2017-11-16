from src.node import Node


class TestNode(object):

    def test_assign_data(self):
        test_node = Node(123)
        assert test_node.data == 123

    def test_assign_next(self):
        test_node = Node(123)
        test_node2 = Node(456, test_node)

        assert test_node2.nextNode.data == 123

    def test_eq_same(self):
        test_node = Node(123)
        test_node2 = Node(123)

        assert test_node._eq(test_node2) == True

    def test_eq_diff(self):
        test_node = Node(123)
        test_node2 = Node(456)

        assert test_node._eq(test_node2) == False
