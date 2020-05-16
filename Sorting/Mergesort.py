def merge(s1, s2, s):
    """Merge two sorted Python lists S1 and S2 into properly sized list S"""
    i = j = 0
    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i + j] = s1[i]
            i += 1
        else:
            s[i + j] = s2[j]
            j += 1

def merge_sort(s):
    """Sort the elements of Python list S using the merge-sort algorithm"""
    if len(s) < 2: # base case
        return
    else:
        s1 = s[:len(s) // 2]
        merge_sort(s1)
        s2 = s[len(s) // 2:]
        merge_sort(s2)
        merge(s1, s2, s) # combine the results

def merge_iter(src, result, start, inc):
    """Merge src[start:start+inc] and src[start+inc:start+2*inc] into result"""
    i, j, k = start, start + inc, start
    end_i, end_j = start + inc, min(start + 2 * inc, len(src))
    while i < end_i and j < end_j:
        if src[i] < src[j]:
            result[k] = src[i]
            i += 1
        else:
            result[k] = src[j]
            j += 1
        k += 1
    if i < end_i:
        result[k:end_j] = src[i:end_i]
    elif j < end_j:
        result[k:end_j] = src[j:end_j]
import math
def merge_sort_iter(s):
    """Sort the elements of Python list S using the merge-sort algorithm"""
    n = len(s)
    logn = math.ceil(math.log(n, 2))
    src, dest = s, [None] * n # make temporary storage for dest

    for i in (2**k for k in range(logn)): # pass i creates all runs of length 2i
        for j in range(0, n, 2 * i): # each pass merges two length i runs
            merge_iter(src, dest, j, i)
        src, dest = dest, src
    if s is not src:
        s[0:n] = src[0:n] # additional copy to get results to S

if __name__ == "__main__":
    s = [43,12,5,12,65,34,53]
    merge_sort_iter(s)
    print(s)
