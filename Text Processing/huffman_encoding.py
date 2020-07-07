class TreeNode:
    def __init__(self, val, freq, left = None, right = None):
        self._val = val
        self._freq = freq
        self._left = left
        self._right = right

    def __lt__(self, other):
        if self._freq == other._freq:
            if self._val == None and other._val == None:
                return True
            elif self._val == None and other._val != None:
                return False
            elif self._val != None and other._val == None:
                return True
            else:
                return self._val < other._val
        return self._freq < other._freq

from collections import Counter
from heapq import heappush, heappop
def huffman_encoding(X):
    counter = Counter(X)
    hq = []
    for key in counter:
        heappush(hq, TreeNode(key, counter[key]))

    while len(hq) > 1:
        left = heappop(hq)
        right = heappop(hq)
        heappush(hq, TreeNode(None, left._freq + right._freq, left, right))
    T = heappop(hq)
    return T

if __name__ == "__main__":
    X = "a fast runner need never be afraid of the dark"
    print(huffman_encoding(X)._left._right._left._val)
    
