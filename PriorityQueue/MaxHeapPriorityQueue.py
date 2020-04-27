from HeapPriorityQueue import HeapPriorityQueue

class MaxHeapPriorityQueue(HeapPriorityQueue):
    """A max-oriented priority queue extends with a min-oriented priority queue"""
    # -------- nonpublic utilities --------
    def _upheap(self, i):
        while i > 0:
            idx_parent = self._parent(i)
            if self._data[i] > self._data[idx_parent]:
                self._swap(i, idx_parent)
                i = idx_parent
            else:
                break
    def _downheap(self, i):
        while i <= len(self._data) - 1:
            left, right, big_child = self._left(i), self._right(i), i
            if left and self._data[left] > self._data[big_child]:
                big_child = left
            if right and self._data[right] > self._data[big_child]:
                big_child = right
            if big_child != i:
                self._swap(i, big_child)
                i = big_child
            else:
                break
    
    # -------- public methods --------
    def __init__(self, contents = ()):
        super().__init__(contents)

    def max(self):
        if len(self._data) == 0:
            raise ValueError("Empty Priority Queue")
        return self._data[0]._key, self._data[0]._value

    def remove_max(self):
        self._swap(0, -1)
        answer = self._data.pop()
        self._downheap(0)
        return answer._key, answer._value

if __name__ == "__main__":
    pq = MaxHeapPriorityQueue([(3, "kb"), (2,"mj"), (5,"sd"), (4,"we")])
    print(pq.max())
    pq.add(1,"dfgdfg")
    while len(pq) != 0:
        print(pq.remove_max())





























        
