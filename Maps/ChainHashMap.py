from HashMapBase import HashMapBase
from UnsortedTableMap import UnsortedTableMap

class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution"""
    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if not bucket:
            raise KeyError("Key Error: " + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k , v):
        if not self._table[j]: # unoccupied bucket
            self._table[j] = UnsortedTableMap()
        if k not in self._table[j]: # a new key
            self._n += 1 # increase the size by 1
        self._table[j][k] = v

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if not bucket:
            raise KeyError("Key Error: " + repr(k))
        del bucket[k] # may raise KeyError

    def __iter__(self):
        for bucket in self._table:
            if bucket:
                for key in bucket:
                    yield key


if __name__ == "__main__":
    m = ChainHashMap(10)
    m["s"] = "sj"
    m["euro"] = "sfsf"
    for key in m:
        print("key: {}, value: {}".format(key, m[key]))
    m["cny"] = "ss"
    print(len(m))
                    
        
