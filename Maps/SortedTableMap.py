from MapBase import Mapbase

class SortedTableMap(Mapbase):
    """Map implementation using a sorted table"""
    #----------------------------- nonpublic behaviors -----------------------------
    def _find_index(self, k, lo, hi):
        """Return index of the leftmost item with key greater than or equal to k.
        Return high + 1 if no such item qualifies
        That is, j will be returned such that:
        all items of slice table[low:j] have key < k
        all items of slice table[j:high+1] have key >= k
        """
        while lo <= hi:
            mid = (lo + hi) // 2
            if self._table[mid]._key == k: # find the key
                return mid
            elif self._table[mid]._key < k:
                lo = mid + 1 # search for the right half
            else:
                hi = mid - 1 # search for the left half
        return hi + 1

    #----------------------------- public behaviors -----------------------------
    def __init__(self):
        self._table = []

    def __len__(self):
        return len(self._table)

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)"""
        i = self._find_index(k, 0, len(self._table) - 1)
        if i == len(self._table) or self._table[i]._key != k:
            raise KeyError("Key Error: " + repr(k))
        return self._table[i]._value

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present"""
        i = self._find_index(k, 0, len(self._table) - 1)
        if i == len(self._table): # append a new k-v pair at the end
            self._table.append(self._Item(k, v))
        elif self._table[i]._key != k: # insert a new k-v pair
            self._table.insert(i, self._Item(k, v))
        else:
            self._table[i]._value = v # key exists, update the value

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)"""
        i = self._find_index(k, 0, len(self._table) - 1)
        if i == len(self._table) or self._table[i]._key != k:
            raise KeyError("Key Error: " + repr(k))
        self._table.pop(i)

    def __iter__(self):
        """Generate keys of the map ordered from minimum to maximum"""
        for item in self._table:
            yield item._key

    def __reversed__(self):
        """Iterate all keys of the map in reverse order"""
        for item in self._table[::-1]:
            yield item._key

    def find_min(self):
        """Return the (key,value) pair with minimum key(or None, if map is empty)"""
        if len(self._table) == 0:
            return None
        return self._table[0]._key, self._table[0]._value

    def find_max(self):
        """Return the (key,value) pair with maximum key(or None, if map is empty)"""
        if len(self._table) == 0:
            return None
        return self._table[-1]._key, self._table[-1]._value

    def find_lt(self, k):
        """Return the (key,value) pair with the greatest key
        that is strictly less than k (or None, if no such item exists)
        """
        i = self._find_index(k, 0, len(self._table) - 1)
        if i == 0:
            return None
        return self._table[i - 1]._key, self._table[i - 1]._value

    def find_gt(self, k):
        """Return the (key,value) pair with the least key
        that is strictly greater than k (or None, if no such item exists)
        """
        i = self._find_index(k, 0, len(self._table) - 1)
        if i < len(self._table) and self._table[i]._key == k:
            i += 1 # find the next key
        if i < len(self._table):
            return self._table[i]._key, self._table[i]._value
        return None
        

    def find_ge(self, k):
        """Return (key,value) pair with least key greater than or equal to k"""
        i = self._find_index(k, 0, len(self._table) - 1)
        if i == len(self._table):
            return None
        return self._table[i]._key, self._table[i]._value

    def find_le(self, k):
        """Return the (key,value) pair with the greatest key
        that is less than or equal to k (or None, if no such item exists)
        """
        i = self._find_index(k, 0, len(self._table) - 1)
        if i == len(self._table) or (i > 0 and self._table[i]._key != k): # no such key exists
            return self._table[i - 1]._key, self._table[i - 1]._value
        elif self._table[i]._key == k: # the key exists
            return self._table[i]._key, self._table[i]._value
        else: # i == 0 and self._table[i]._key != k
            return None

    def find_range(self, start = None, stop = None):
        """Iterate all (key,value) pairs with start <= key < stop
        If start is None, iteration begins with minimum key;
        if stop is None, iteration concludes with maximum key
        """
        if not start:
            i = 0
        else:
            i = self._find_index(start, 0, len(self._table) - 1) # find the first start
        while i < len(self._table) and (not stop or self._table[i]._key < stop):
            yield self._table[i]._key, self._table[i]._value
            i += 1

if __name__ == "__main__":
    st = SortedTableMap()
    st[5] = "sf"
    st[2] = "dsd"
    st[1] = "fgjdfg"
    st[8] = "sfsdff"
    st[9] = "saf"
    
    for key, value in iter(st.find_range(10,3)):
        print("key: {}, value: {}".format(key, value))
        
        

    
        
            
        
        





















        
        
