def LCS(X, Y):
    """Return table such that L[j][k] is length of LCS for X[0:j] and Y[0:k]
    L[j][k] = L[j - 1][k - 1] + 1, if X[j] == Y[k];
    L[j][k] = max(L[j - 1][k], L[j][k - 1]), if X[j] != Y[k]"""
    n, m = len(X), len(Y)
    L = [[0] * (m + 1) for _ in range(n + 1)]
    for j in range(n):
        for k in range(m):
            if X[j] == Y[k]:
                L[j + 1][k + 1] = L[j][k] + 1
            else:
                L[j + 1][k + 1] = max(L[j][k + 1], L[j + 1][k])
    j, k = n, m
    res = []
    while L[j][k] > 0:
        if X[j - 1] == Y[k - 1]:
            res.append(X[j - 1])
            j -= 1
            k -= 1
        else:
            # we can find another solution if we use >=
            if L[j - 1][k] > L[j][k - 1]: 
                j -= 1
            else:
                k -= 1
    return "".join(reversed(res))

if __name__ == "__main__":
    X = "GTTCCTAATA"
    Y = "CGATAATTGAGA"
    print(LCS(X, Y))
