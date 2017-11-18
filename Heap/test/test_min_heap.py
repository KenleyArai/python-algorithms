from src.heap import Heap


class TestMinHeap:

    def test_init(self):
        h = Heap()
        assert h._head._data == None and h._head._left == None and h._head._right == None and h._type == 'min'

    def test_push(self):
        pass

    def test_pop(self):
        pass

    def test_empty(self):
        pass

    def test_peek(self):
        pass

    def test_size(self):
        pass

    def test_heapify(self):
        pass

    def test_sift_up(self):
        pass

    def test_sift_down(self):
        pass
