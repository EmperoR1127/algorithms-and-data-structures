def find_boyer_moore(t, p):
    """Return the lowest index of T at which substring P begins (or else -1)"""
    n, m = len(t), len(p)
    if m == 0:
        return 0 # trivial search for empty string
    last = {} # the last apperance of a char in p
    for i in range(m):
        last[p[i]] = i # later occurrence overwrites
    
    i, k = m - 1, m - 1
    while i < n:
        if t[i] == p[k]: # a matching character
            if k == 0:
                return i # pattern begins at index i of text
            else:
                k -= 1 # examine previous character
                i -= 1 # of both T and P
        else:
            j = last.get(t[i], -1) # last(T[i]) is -1 if not found
            i += m - min(k, j + 1) # case analysis for jump step
            k = m - 1 # restart at end of pattern
    return -1
            
def find_boyer_moore_2(t, p):
    n = len(t)
    m = len(p)
    last = {}
    for i in range(m):
        last[p[i]] = i
    i = m - 1
    k = m - 1
    while i < n:
        while t[i] == p[k]:
            if k == 0:
                return i
            i -= 1
            k -= 1
        # retrieve the last appearance of t[i] in p
        j = last.get(t[i], -1)
        if j == -1: # t[i] is not in p
            i += m # no match between i + m
        else: # t[i] is in p
            if j < k: # t[i] appears before p[k]
                i += m -(j + 1)
            else: # t[i] appears after p[k]
                i += m - k # shift 1 unit
        k = m - 1
    return -1


if __name__ == "__main__":
    print(find_boyer_moore_2("abacaabaccabacabaabb","abacab"))
