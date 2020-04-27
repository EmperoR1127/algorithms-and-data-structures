from MapBase import Mapbase

class UnsortedTableMap(Mapbase):
    """Map implementation using an unordered list"""
    def __init__(self):
        self._table = []

    def __len__(self):
        return len(self._table)

    def is_empty(self):
        return len(self) == 0
    
    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present"""
        for item in self._table:
            if item._key == k: # the key is already in the map
                item._value = v # overwrite the value
                return
        self._table.append(self._Item(k, v)) # insert a new key-value pair

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)"""
        for item in self._table:
            if item._key == k:
                return item._value
        raise KeyError("Key Error: " + repr(k))

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)"""
        for i in range(len(self._table)):
            if self._table[i]._key == k:
                self._table.pop(i)
                return
        raise KeyError("Key Error: " + repr(k))

    def __iter__(self):
        """Generate iteration of the map s keys"""
        for item in self._table:
            yield item._key

if __name__ == "__main__":
    m = UnsortedTableMap()
    m["s"] = "sj"
    m["euro"] = "sfsf"
    for key in m:
        print("key: {}, value: {}".format(key, m[key]))











    
