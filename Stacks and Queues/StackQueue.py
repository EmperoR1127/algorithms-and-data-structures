from ArrayStack import ArrayStack

class StackQueue():
    """Implement ADT queue using two stacks"""
    def __init__(self):
        self._s = ArrayStack()
        self._t = ArrayStack()

    def __len__(self):
        return len(self._s) + len(self._t)

    def is_empty(self):
        return self._s.is_empty() and self._t.is_empty()

    def enqueue(self, value):
        self._s.push(value)

    def dequeue(self):
        if not self._t.is_empty():
            return self._t.pop()
        else:
            if self._s.is_empty():
                raise ValueError("Empty Queue")
            else:
                while not self._s.is_empty():
                    self._t.push(self._s.pop())
                return self._t.pop()
