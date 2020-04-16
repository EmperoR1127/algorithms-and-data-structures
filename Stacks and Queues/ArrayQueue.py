class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an ArrayQueue with default capacity"""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of element in the queue"""
        return self._size

    def is_empty(self):
        return self._size == 0

    def dequeue(self):
        if self.is_empty():
            raise ValueError("The queue is empty")
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2) # shrink the list
        value, self._data[self._front] = self._data[self._front], None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return value

    def first(self):
        if self.is_empty():
            raise ValueError("The queue is empty")
        return self._data[self._front]

    def enqueue(self, value):
        """Enqueue the value at the end of the queue"""
        if self._size == len(self._data): # the list is full
            self._resize(2 * len(self._data)) # double the size of the list
        self._data[(self._front + self._size) % len(self._data)] = value
        self._size += 1


    def _resize(self, c):
        """Resize the internal array with capacity c"""
        temp_array = [None] * c
    
        for i in range(self._size):
            temp_array[i] = self._data[self._front]
            self._front = (self._front + 1) % len(self._data)
        self._data = temp_array
        self._front = 0


if __name__ == "__main__":
    q = ArrayQueue()
    q.enqueue(4)
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(1)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(9)
    q.enqueue(10)
    q.enqueue(11)
    q.enqueue(12)
    q.enqueue(13)
    q.enqueue(14)
    q.enqueue(15)
    q.enqueue(16)
    q.enqueue(52)
    q.enqueue(42)
    while not q.is_empty():
        print(q.dequeue())




    
