from Algorithms import heapsort, quicksort, mergesort, insertionsort


def get_test_arrays():
    return [1, 3, 4, 6, 7, 10], [10, 4, 6, 1, 3, 7]


class TestSort:

    def test_heapsort(self):
        sorted_A, unsorted_A = get_test_arrays()
        assert heapsort(unsorted_A) == sorted_A

    def test_quicksort(self):
        sorted_A, unsorted_A = get_test_arrays()
        quicksort(unsorted_A)
        assert unsorted_A == sorted_A

    def test_insertionsort(self):
        sorted_A, unsorted_A = get_test_arrays()
        insertionsort(unsorted_A)  # Inplace sort
        assert unsorted_A == sorted_A

    def test_mergesort(self):
        sorted_A, unsorted_A = get_test_arrays()
        mergesort(unsorted_A)
        assert unsorted_A == sorted_A
