from PriorityQueueBase import PriorityQueueBase

class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap"""
    # -------- nonpublic utilities --------
    def _parent(self, i):
        """Return the index of the parent of item locating in index i"""
        return (i - 1) // 2
    def _left(self, i):
        """Return the index of the left child of item locating in index i"""
        return 2 * i + 1 if 2 * i + 1 < len(self._data) else None

    def _right(self, i):
        """Return the index of the left child of item locating in index i"""
        return 2 * i + 2 if 2 * i + 2 < len(self._data) else None

    def _upheap(self, i):
        """Upheap from index i"""
        idx_parent = self._parent(i) # the index of parent
        if i > 0 and self._data[i] < self._data[idx_parent]:
            # swap the item
            self._data[i], self._data[idx_parent] = self._data[idx_parent], self._data[i]
            self._upheap(idx_parent) # recursively upheap the parent

    def _downheap(self, i):
        """Downheap from index i"""
        if i == len(self._data) - 1: # i is the last item, no need to downheap
            return
        left, right = self._left(i), self._right(i)
        min_child = 0 # the min of two children, if any
        if not left: # no children
            return
        # only one child or left child is smaller than right child
        # heap is a complete binary tree, so if a node only has one child
        # it should be its left child
        elif (left and not right) or self._data[left] < self._data[right]: 
            min_child = left
        else:
            min_child = right
        if self._data[i] > self._data[min_child]: # swap the item
            self._data[i], self._data[min_child] = self._data[min_child], self._data[i]
            self._downheap(min_child) # recursively downheap the child

    def _heapify(self):
        # no need to downheap the leaf node
        start = self._parent(len(self._data) - 1)
        for i in range(start, -1, -1): # construct the heap from bottom up
            self._downheap(i)
        

    # -------- public methods --------
    def __init__(self, contents = ()):
        """Create a new priority queue. By default, queue will be empty.
        If contents is given, it should be as an iterable sequence
        of (k,v) tuples specifying the initial contents
        """
        self._data = [self._Item(key, value) for key, value in contents]
        if len(self._data) > 1:
            self._heapify()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair"""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key"""
        if self.is_empty():
            raise ValueError("The priority queue is empty")
        item = self._data[0]
        return item._key, item._value

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key"""
        if self.is_empty():
            raise ValueError("The priority queue is empty")
        # swap the first and last item
        self._data[0], self._data[-1]= self._data[-1], self._data[0]
        item = self._data.pop()
        self._downheap(0)
        return item._key, item._value    
        
        
            
if __name__ == "__main__":
    pq = HeapPriorityQueue([(3, "kb"), (2,"mj"), (5,"sd"), (4,"we")])
    print(pq.min())
    pq.add(1,"dfgdfg")
    print(pq.remove_min())
    print(pq.remove_min())
    print(pq.remove_min())
    print(pq.remove_min())
    print(pq.remove_min())
    print(pq.remove_min())


    
        













        
        

    
