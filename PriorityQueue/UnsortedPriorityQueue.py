from PriorityQueueBase import PriorityQueueBase
from PositionalList import PositionalList

class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list"""
    def __init__(self):
        self._data = PositionalList()
    
    def _find_min(self):
        """Return Position of item with minimum key"""
        if self._data.is_empty(): # empty queue
            raise ValueError("Empty Priority Queue")
        small = self._data.first()
        walk = self._data.after(small)
        while walk != None:
            # find a item with smaller key or higher priority
            if small.element() > walk.element(): 
                small = walk
            walk = self._data.after(walk)
        return small

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair"""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key"""
        item = self._find_min().element()
        return item._key, item._value

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key"""
        p = self._find_min() # find the position
        item = self._data.delete(p) # delete the position and return the element
        return item._key, item._value

if __name__ =="__main__":
    pq = UnsortedPriorityQueue()
    pq.add(5,"mj")
    pq.add(3,"kb")
    pq.add(1, "sd")
    pq.add(8,"ff")
    print(pq.min())
    print(pq.remove_min())
    print(pq.min())































        
        
        
