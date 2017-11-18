from src.node import Node


class TestNode:

    def test_creation(self):
        n = Node(123)
        assert n._data == 123 and n._left == None and n._right == None

    def test_gt(self):
        n1 = Node(10)
        n2 = Node(5)
        assert n1 > n2

    def test_lt(self):
        n1 = Node(5)
        n2 = Node(10)
        assert n1 < n2

    def test_eq(self):
        n1 = Node(10)
        n2 = Node(10)
        assert n1 == n2

    def test_bool(self):
        n = Node(10)
        if n:
            assert True
        else:
            assert False and n
        n = Node()
        if n:
            assert False and n
        else:
            assert True
