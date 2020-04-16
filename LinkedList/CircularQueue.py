class CircularQueue:
    """Queue implementation using circularly linked list for storage."""
    #------------------------------- nested Node class----------------------
    class _Node():
        """Lightweight, nonpublic class for storing a singly linked node."""
        def __init__(self, element, next = None):
            __slots__ = "_element", "_next"
            self._element = element
            self._next = next
    #------------------------------- queue methods -------------------------

    def __init__(self):
        self._tail = None # the last node in the queue
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, value):
        node = self._Node(value)
        if self.is_empty(): # enqueue the first node
            node._next = node 
        else:
            node._next = self._tail._next
            self._tail._next = node
        self._tail = node # node will be the tail
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Empty queue")
        node = self._tail._next # the front node
        self._size -= 1
        if self._size == 0:
            self._tail = None # special case, reset tail
        else:
            self._tail._next = node._next
        return node._element

    def front(self):
        if self.is_empty():
            raise ValueError("Empty queue")
        return self._tail._next._element

    def rotate(self):
        if self.is_empty():
            return
        self._tail = self._tail._next


if __name__ == "__main__":
    q = CircularQueue()
    q.enqueue(5)
    q.enqueue(7)
    for i in range(2 * len(q)):
        print(q.front())
        q.rotate()



















    
