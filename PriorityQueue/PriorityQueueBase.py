class PriorityQueueBase:
    """Abstract base class for a priority queue"""
    class _Item:
        """Lightweight composite to store priority queue items"""
        def __init__(self, key, value):
            __slots__ = "_key", "_value"
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key # compare items based on their keys

    def is_empty(self):
        """Return True if the priority queue is empty"""
        return len(self) == 0
            
        
