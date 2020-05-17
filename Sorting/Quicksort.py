from LinkedQueue import LinkedQueue

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
    pivot = s[end] # last element ast pivot
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


if __name__ == "__main__":
    a = [3,5,1,2,9,3,5,2,3,5,12,4]
    inplace_quick_sort(a, 0, len(a) - 1)
    print(a)














