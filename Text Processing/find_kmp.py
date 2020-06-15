def find_kmp(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)
    fail = compute_kmp_fail(P)
    if n > m:
        j, k = 0, 0
        while j < n:
            if T[j] == P[k]: # P[0:1+k] matched thus far
                if k == m - 1: # find the match
                    return j - m + 1
                j += 1 # try to extend match
                k += 1
            elif k > 0:
                k = fail[k - 1] # reuse suffix of P[0:k]
            else:
                j += 1
        return -1

def compute_kmp_fail(p):
    """Utility that computes and returns KMP fail list."""
    m = len(p)
    fail = [0] * m
    j, k = 1, 0
    while j < m: # compute f(j) during this pass, if nonzero
        if p[j] == p[k]: # k + 1 characters match thus far
            fail[j] = k + 1
            k += 1
            j += 1
        elif k > 0: # k follows a matching prefix
            k = fail[k - 1]
        else: # no match found starting at j
            j += 1 
    return fail

if __name__ == "__main__":
    print(find_kmp("abacaabaccabacabaabb","abacab"))
            
