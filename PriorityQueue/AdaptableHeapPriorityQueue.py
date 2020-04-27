from HeapPriorityQueue import HeapPriorityQueue

class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """A locator-based priority queue implemented with a binary heap"""
    #------------------------------ nested Locator class ------------------------------
    class Locator(HeapPriorityQueue._Item):
        """Token for locating an entry of the priority queue"""
        __slots__ = "_index"
        def __init__(self, loc, k ,v):
            super().__init__(k, v)
            self._index = loc
    #------------------------------ nonpublic utilities ------------------------------
    def _swap(self, i, j):
        """Swap two locators locating at index i and j"""
        super()._swap(i, j)
        self._data[i]._index, self._data[j]._index = i, j # reset locator._index

    def _bubble(self, i):
        """Bubble up or down according to the key and the current index"""
        if i > 0 and self._data[i] < self._data[self._parent(i)]:
            self._upheap(i)
        else:
            self._downheap(i)
        
            
    #------------------------------ public methods ------------------------------
    def __init__(self, contents = ()):
        self._data = [self.Locator(i, key, value) for i, (key, value) in enumerate(contents)]
        if len(self._data) > 1:
            self._heapify()

    def add(self, key, value):
        token = self.Locator(len(self._data), key, value)
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

    def remove(self, loc):
        """Remove the item identified by locator loc from the priority queue
        and return its (key,value) pair
        """
        idx = loc._index
        if not (0 <= idx < len(self._data) and self._data[idx] == loc):
            raise ValueError("Invalid locator")
        self._swap(idx, -1) # swap index of loc with the last element
        self._data.pop()
        self._downheap(idx)
        return loc._key, loc._value

    def update(self, loc, k, v):
        """Replace key and value for the item identified by locator loc"""
        idx = loc._index
        if not (0 <= idx < len(self._data) and self._data[idx] == loc):
            raise ValueError("Invalid locator")
        loc._key, loc._value = k, v
        self._bubble(idx)


if __name__ == "__main__":
    pq = AdaptableHeapPriorityQueue([(3, "kb"), (2,"mj"), (5,"sd"), (4,"we")])
    print(pq.min())
    token = pq.add(1,"dfgdfg")
    print(pq.update(token, 10, "ss"))
    print(pq.remove(token))
    while len(pq) != 0:
        print(pq.remove_min())
    
        
        

    


    
            
        
        
