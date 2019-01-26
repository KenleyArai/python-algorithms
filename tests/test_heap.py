from Datastructures import Heap
import random


class TestMinHeap:

    def test_parent(self):
        assert Heap.parent(2) == 1
        assert Heap.parent(6) == 3
        assert Heap.parent(7) == 3

    def test_left(self):
        assert Heap.left(1) == 2
        assert Heap.left(4) == 8

    def test_right(self):
        assert Heap.right(1) == 3
        assert Heap.right(4) == 9

    def test_build_heap(self):
        h = Heap()

        h.build_heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])

        assert h._heap == [float("-inf"), 16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

    def test_insert(self):
        h = Heap()
        h.insert(10)
        h.insert(13)
        assert h._data[0] == 10
        h.insert(20)
        assert h._data[1] == 13
        h.insert(5)
        assert h._data[0] == 5

    def test_pop(self):
        h = Heap()
        h.insert(10)
        h.insert(20)
        h.insert(5)
        h.insert(100)
        h.insert(11)

        min_val = h.pop()

        assert min_val == 5

    def test_is_empty(self):
        h = Heap()
        h.insert(10)
        assert h.is_empty() == False

    def test_peek(self):
        h = Heap()
        h.insert(10)
        h.insert(20)
        h.insert(5)
        h.insert(100)
        h.insert(11)

        assert h.peek() == 100
