class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self):
        """A list used to store data"""
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, value):
        """Push value to the top of the stack"""
        self._data.append(value)

    def pop(self):
        """Delete and return the value on top of the stack
        raise an exception when the stack is empty
        """
        if self.is_empty():
            raise ValueError("The stack is empty")
        return self._data.pop()

    def top(self):
        """Return the value on top of the stack
        raise an exception when the stack is empty
        """
        if self.is_empty():
            raise ValueError("The stack is empty")
        return self._data[-1]

    def __str__(self):
        return str(self._data)
