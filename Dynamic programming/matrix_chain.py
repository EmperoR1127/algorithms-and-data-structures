def matrix_chain(d):
    """d is a list of n+1 numbers such that size of kth matrix is d[k]-by-d[k+1]
    Let N[i, j] denotes the minimum number of mulitiplications needs to perform
    in order to multiply AiA(i+1)...Aj.
    Then N[i, j] = min(N[i, k] + N[k + 1, j] + d[i]*d[k + 1]*d[j])"""
    n = len(d) - 1
    res = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        res[i][i] = 0
        
    for i in range(n):
        for diff in range(1, n - i):
            j = i + diff
            for k in range(i, j):
                res[i][j] = min(res[i][j], res[i][k] + res[k + 1][j] + d[i] * d[k + 1] * d[j + 1])
    
    return res[0][-1]


if __name__ == "__main__":
    d = [10, 50, 20, 30]
    print(matrix_chain(d))
    
