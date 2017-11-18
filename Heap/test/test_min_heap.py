from src.heap import Heap
import random


class TestMinHeap:

    def test_push(self):
        h = Heap()
        h.push(10)
        h.push(13)
        assert h._data[0] == 10
        h.push(20)
        assert h._data[1] == 13
        h.push(5)
        assert h._data[0] == 5

    def test_pop(self):
        h = Heap()
        h.push(10)
        h.push(20)
        h.push(5)
        h.push(100)
        h.push(11)

        min_val = h.pop()

        assert min_val == 5

    def test_empty(self):
        h = Heap()
        h.push(10)
        assert h.is_empty() == False

    def test_peek(self):
        h = Heap()
        h.push(10)
        h.push(20)
        h.push(5)
        h.push(100)
        h.push(11)

        assert h.peek() == 5

    def test_size(self):
        h = Heap()
        h.push(10)
        h.push(20)
        h.push(5)
        h.push(100)
        h.push(11)

        assert h.size() == 5
