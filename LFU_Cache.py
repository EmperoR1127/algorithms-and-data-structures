class LFUCache:
    # -----nested _DoublyLinkedList class
    class _DoublyLinkedList:
        # -----nested _Node class
        class _Node:
            """Light weight doubly linked list class"""
            def __init__(self, value, pre = None, next = None):
                __slots__ = "_value", "_pre", "_next"
                self._value = value
                self._pre = pre
                self._next = next
            
        def __init__(self):
            self._header = self._Node(None) # head sentinal
            self._tailer = self._Node(None) # tail sentinal
            self._header._next = self._tailer
            self._tailer._pre = self._header
            self._size = 0
            
        def __len__(self):
            return self._size
        
        # ----- nonpublic utilities -----
        def _delete(self, node):
            """Delete and return the value of the given node"""
            if self._size == 0:
                raise ValueError("Empty doubly list")
            pre, next = node._pre, node._next
            pre._next, next._pre = next, pre
            self._size -= 1
            return node._value
        
        def _insert_last(self, key: int):
            """Insert and return a node before the last node"""
            pre = self._tailer._pre
            node = self._Node(key, pre, self._tailer)
            pre._next, self._tailer._pre = node, node
            self._size += 1
            return node
        

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._min_count = 0
        self._cache = {}
        self._lists = [self._DoublyLinkedList()]

    def get(self, key: int) -> int:
        """update the frequency and node after using the key
        insert a node at the end of the list of higher frequency
        """
        if self._capacity == 0 or key not in self._cache:
            return -1
        value, node, frequency = self._cache[key][0], self._cache[key][1], self._cache[key][2]
        frequency = self._update(node, frequency) # update the frequency
        node = self._lists[frequency - 1]._insert_last(key) # add a node in the list
        self._cache[key] = (value, node, frequency)
        return value
        
    def put(self, key: int, value: int) -> None:
        """an exisiting key with a frequency, q, will be in the self._lists[q - 1]
        update the frequency and node after using the key
        otherwise a new key will be the last node of self._lists[0], meaning the frequency is 1.
        if reached the capacity, delete the first node in self._lists[self._min_count - 1]
        anytime put a new key to the dict, reset the self._min_count to 1
        """
        if self._capacity == 0:
            return
        node, frequency = None, 0
        if key in self._cache: # an exisiting key
            node, frequency = self._cache[key][1], self._cache[key][2]
            frequency = self._update(node, frequency)
        else: # a new key
            if len(self._cache) == self._capacity: # reach the capacity
                min_link = self._lists[self._min_count - 1]
                old_key = min_link._delete(min_link._header._next) # retrive the key with the least frequency
                del self._cache[old_key] # delete the key
            frequency = 1 # initialize the frequency
            self._min_count = 1 # reset the min_count
        node = self._lists[frequency - 1]._insert_last(key) # add a node in the list
        self._cache[key] = (value, node, frequency)
        
    # ----- nonpublic utilities -----
    def _update(self, node, frequency: int) -> int:
        """delete the node from self._lists[frequency - 1] and then increase an existing key's frequency by 1
        enlarge the self._lists, if necessary
        if the given frequency is the same as self._min_count and self._lists[self._min_count - 1] is empty
        reset the self._min_count to 1
        return the node and frequency
        """
        self._lists[frequency - 1]._delete(node) # delete the node in the old list
        # list at minimal frequency is empty
        if frequency == self._min_count and len(self._lists[self._min_count - 1]) == 0:
            self._min_count += 1
        if len(self._lists) == frequency: # enlarge the list
            self._lists.append(self._DoublyLinkedList())
        frequency += 1
        return frequency
            
if __name__ == "__main__":
    cache = LFUCache(6)
    print(cache.put(10,13))
    print(cache.put(3,17))
    print(cache.put(6,11))
    print(cache.put(10,5))
    print(cache.put(9,10))
    print(cache.get(13))
    print(cache.put(2,19))
    print(cache.get(2))
    print(cache.get(3))
    print(cache.put(5,25))
    print(cache.get(8))
    print(cache.put(9,2))
    print(cache.put(5,5))
    print(cache.put(1,30))
    print(cache.get(11))
    print(cache.put(9,12))
    print(cache.get(7))
    print(cache.get(5))
    
    
    
    


















    
