def permutation(n):
    """Return the permutations of range(n + 1)"""
    res = []
    
    # -------- nonpublic helper method --------
    def _helper(selected, selectable):
        """
        selected: the num selected so far
        selectable: range(1, n + 1)
        """
        if len(selected) == n: # find a permutation
            res.append([i for i in selected])
            return

        for i in selectable:
            if i not in selected: # choose a non-repeated number
                selected.append(i) 
                _helper(selected, selectable) # next level iteration
                selected.pop() # backtrack
    
    selectable = [i for i in range(1, n + 1)]
    _helper([], selectable)
    return res

if __name__ == "__main__":
    for per in permutation(5):
        print(per)
    
        
