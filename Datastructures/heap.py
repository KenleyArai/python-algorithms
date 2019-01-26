
class Heap:

    def __init__(self, heaptype='max'):
        self._heap = [float("inf") if heaptype == 'min' else float("-inf")]
        self._type = heaptype
        self._size = 0

    def build_heap(self, A):
        self._size = len(A)
        self._heap = [float("-inf")] + A[:]

        # Building the heap from the bottom up
        # self._heap[i:len(A)] is a heap before each iteration
        for i in range(len(A) >> 1, 0, -1):
            self.heapify(i)
        # When we terminate self._heap[0:len(A)] => self._heap is a heap

    def heapify(self, i):
        left = self.left(i)
        right = self.right(i)

        largest = float("-inf")

        if left <= self._size and self._heap[left] > self._heap[i]:
            largest = left
        else:
            largest = i

        if right <= self._size and self._heap[right] > self._heap[largest]:
            largest = right

        if largest != i:
            self._heap[i], self._heap[largest] = self._heap[largest], self._heap[i]
            self.heapify(largest)

    def is_empty(self):
        return self._size == 0

    @staticmethod
    def parent(i):
        return i >> 1

    @staticmethod
    def left(i):
        return i << 1

    @staticmethod
    def right(i):
        return (i << 1) + 1
