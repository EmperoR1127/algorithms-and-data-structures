from random import choice
def quick_select(s, k):
    """Return the kth smallest element of list S, for k from 1 to len(S)"""
    if len(s) == 1:
        return s[0]
    pivot = choice(s) # pick random pivot element from S
    small = [c for c in s if c < pivot] # elements less than pivot
    equal = [c for c in s if c == pivot] # elements equal to pivot
    large = [c for c in s if c > pivot] # elements greater than pivot
    if k <= len(small): # kth smallest lies in L
        return quick_select(small, k)
    elif len(small) < k <= len(small) + len(equal):
        return pivot # kth smallest equal to pivot
    else:
        return quick_select(large, k - len(small) - len(equal))

if __name__ == "__main__":
    s = [1,3,4,5,9,7]
    print(quick_select(s,6))
