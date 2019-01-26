from Datastructures import Heap

# TODO:  Inplace


def heapsort(A):
    h = Heap()
    h.build_heap(A)

    for i in range(h._size, 1, -1):
        h._heap[1], h._heap[i] = h._heap[i], h._heap[1]
        h._size -= 1
        h.heapify(1)

    return h._heap[1:]
