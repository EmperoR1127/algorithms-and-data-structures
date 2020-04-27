from MapBase import Mapbase
from random import randrange

class HashMapBase(Mapbase):
    """Abstract base class for map using hash-table with MAD compression"""
    def __init__(self, cap, p = 109345121):
        """Create an empty hash-table map.”””"""
        self._table = [None] * cap
        self._prime = p
        self._n = 0 # the size of the map
        self._scale = 1 + randrange(p - 1) # scale from 1 to p-1 for MAD
        self._swift = randrange(p - 1) # shift from 0 to p-1 for MAD

    def _hash_function(self, k):
        return ((hash(k) * self._scale + self._swift) % self._prime) % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k) # may raise KeyError

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n * 2 > len(self._table): # load factor is > 0.5
            self._resize(2 * len(self._table) - 1) # number 2ˆx - 1 is often prime

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k) # may raise KeyError
        self._n -= 1

    def _resize(self, c):
        """resize bucket array to capacity c"""
        old = list(self.items())
        self._table = [None] * c
        self._n = 0 # n recomputed during subsequent adds
        for k, v in old:
            j = self._hash_function(k)
            self[j] = v











    
            
        
