from HashMapBase import HashMapBase

class ProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision resolution"""
    _AVAIL = object() # sentinal marks locations of previous deletions

    def _is_available(self, j):
        """Return True if index j is available in table"""
        return not self._table[j] or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """Search for key k in bucket at index j
        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location
        If no match found, success is False and index denotes first available slot
        """
        first = None
        while True:
            if self._is_available(j):
                if not first:
                    first = j
                if not self._table[j]:
                    return False, first
            elif k == self._table[j]._key:
                return True, j
            j = (j + 1) % len(self._table)

    def _bucket_getitem(self, j, k):
        success, j = self._find_slot(j, k)
        if not success:
            raise KeyError("Key Error: " + repr(k))
        return self._table[j]._value

    def _bucket_setitem(self, j, k , v):
        success, j = self._find_slot(j, k)
        if not success: # no such key is found
            self._table[j] = self._Item(k, v)
            self._n += 1
        else:
            self._table[j]._value = v

    def _bucket_delitem(self, j, k):
        success, j = self._find_slot(j, k)
        if not success:
            raise KeyError("Key Error: " + repr(k))
        self._table[j] = ProbeHashMap._AVAIL # mark as a sentinal

    def __iter__(self):
        for i in range(len(self._table)):
            if not self._is_available(i):
                yield self._table[i]._key

if __name__ == "__main__":
    m = ProbeHashMap(10)
    m["s"] = "sj"
    m["euro"] = "sfsf"
    m["cny"] = "ss"
    m["s"] = "modified"
    for key in m:
        print("key: {}, value: {}".format(key, m[key]))
    print(len(m))            

















        
                
        
    
