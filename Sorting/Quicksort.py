from LinkedQueue import LinkedQueue
from random import choice

def quick_sort(s):
    """”””Sort the elements of queue S using the quick-sort algorithm"""
    n = len(s)
    if n < 2: # base case, return immediately
        return
    lt = LinkedQueue()
    eq = LinkedQueue()
    gt = LinkedQueue()
    pivot = s.front()
    
    while not s.is_empty():
        if s.front() < pivot: # put smaller elements in the lt
            lt.enqueue(s.dequeue())
        elif s.front() > pivot: # put larger elements in the gt
            gt.enqueue(s.dequeue())
        else: # put equal elements in the eq
            eq.enqueue(s.dequeue())
    # conquer (with recursion)
    quick_sort(lt) # sort elements less than p
    quick_sort(gt) # sort elements greater than p

    # concatenate results
    while not lt.is_empty():
        s.enqueue(lt.dequeue())
    while not eq.is_empty():
        s.enqueue(eq.dequeue())
    while not gt.is_empty():
        s.enqueue(gt.dequeue())

def inplace_quick_sort(s, start, end):
    """Sort the list from s[start] to s[end] inclusive using the quick-sort algorithm"""
    if start >= end: # base case
        return
    p = choice(range(start, end + 1))
    pivot = s[p] # select the pivot randomly
    s[end], s[p] = s[p], s[end] # put the pivot at the end of list
    left, right = start, end - 1
    while left <= right:
        if s[left] > pivot and s[right] <= pivot:
            s[left], s[right] = s[right], s[left] # swap two elements
        if s[left] <= pivot:
            left += 1
        if s[right] > pivot:
            right -= 1
    # put pivot into its final place (currently marked by left index)
    s[left], s[end] = s[end], s[left]
    # make recursive calls
    inplace_quick_sort(s, start, left - 1)
    inplace_quick_sort(s, left + 1, end)

def inplace_3sets_quick_sort(s, start, end):
    """Sort the list from s[start] to s[end] inclusive using the quick-sort algorithm
    divide the list into three parts: small, equal and large
    """
    if start >= end: # base case
        return
    pivot = choice(s[start:end + 1]) # select the pivot randomly
    i, j, k = start, start, start
    while j <= end and s[j] != pivot: # find the leftmost index of pivot
        j += 1
    s[i], s[j] = s[j], s[i] # swap the pivot and the first element in the list
    j = i
    while k <= end:
        if s[k] < pivot:
            s[i], s[k] = s[k], s[i]
            i += 1
        if s[k] == pivot:
            s[j], s[k] = s[k], s[j]
            j += 1
        k += 1
    #print("pivot = {}, s = {}".format(pivot, s[start:end+1]))
    inplace_3sets_quick_sort(s, start, i - 1)
    inplace_3sets_quick_sort(s, j, end)
    

if __name__ == "__main__":
    a = [3,5,1,2,9,3,5,2,3,5,12,4]
    inplace_3sets_quick_sort(a, 0, len(a) - 1)
    print(a)














