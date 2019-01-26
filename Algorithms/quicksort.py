def quicksort(A):
    def part(lo, hi):
        pivot = A[hi]
        i = lo

        for j in range(lo, hi):
            if A[j] < pivot:
                A[j], A[i] = A[i], A[j]
                i += 1
        A[i], A[hi] = A[hi], A[i]
        return i

    def _quicksort(lo, hi):
        if lo < hi:
            p = part(lo, hi)
            _quicksort(lo, p-1)
            _quicksort(p+1, hi)

    _quicksort(0, len(A)-1)
