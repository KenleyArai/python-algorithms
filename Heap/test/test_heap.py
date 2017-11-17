from src.heap import Heap


class TestHeap:

    def test_init(self):
        h = Heap()
        assert h._head._data == None and h._head._left == None and h._head._right == None and h._type == 'min'
