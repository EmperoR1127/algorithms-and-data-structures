from PriorityQueueBase import PriorityQueueBase
from PositionalList import PositionalList

class SortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a sorted list"""
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def min(self):
        if self.is_empty():
            raise ValueError("Empty Priority Queue")
        item = self._data.first().element()
        return item._key, item._value

    def remove_min(self):
        if self.is_empty():
            raise ValueError("Empty Priority Queue")
        item = self._data.delete(self._data.first())
        return item._key, item._value

    def add(self, key, value):
        new_item = self._Item(key, value)
        walk = self._data.last()
        # walk backwards for smaller key
        while walk != None and new_item < walk.element():
            walk = self._data.before(walk)
        if walk:
            self._data.add_after(new_item, walk)
        else: # walk is the header
            self._data.add_first(new_item)


if __name__ =="__main__":
    pq = SortedPriorityQueue()
    pq.add(5,"mj")
    pq.add(3,"kb")
    pq.add(1, "sd")
    pq.add(8,"ff")
    print(pq.min())
    print(pq.remove_min())
    print(pq.min())
        
                
