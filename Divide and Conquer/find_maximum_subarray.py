def find_maximum_subarray(nums, low, high):
    """Returns the contiguous subarray with the maximum sum
    the maximum subarray must be one of the following:
    entirely in the subarray A[low:mid], so that low <= i<= j<= mid,
    entirely in the subarray A[mid + 1:high], so that mid < i <=j <= high, or
    crossing the midpoint, so that low <= i <= mid < j <= high."""
    if low == high:
        return (low, high, nums[low])
    mid = (low + high) // 2
    left = find_maximum_subarray(nums, low, mid)
    right = find_maximum_subarray(nums, mid + 1, high)
    crossing = find_maximum_crossing_subarray(nums, low, high)
    max_sum = max(left[2], right[2], crossing[2])
    if max_sum == left[2]:
        return left
    elif max_sum == right[2]:
        return right
    else:
        return crossing


def find_maximum_crossing_subarray(nums, lo, hi):
    """Returns the subarray with the maxium sum such that
    the subarray crosses the mid point of the original array"""
    mid = (lo + hi) // 2
    left, s, max_sum_left = mid, 0, -float("inf")
    for i in range(mid, lo - 1, -1):
        s += nums[i]
        if s > max_sum_left:
            max_sum_left = s
            left = i
    right, s, max_sum_right = mid + 1, 0, -float("inf")
    for j in range(mid + 1, hi + 1):
        s += nums[j]
        if s > max_sum_right:
            max_sum_right = s
            right = j
    return (left, right, max_sum_left + max_sum_right)


if __name__ == "__main__":
    nums = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    nums = [13,23,2,12,-1,-1,-1,-1,-11,-34,-23]
    #print(find_maximum_crossing_subarray(nums, 0, len(nums) - 1))
    print(find_maximum_subarray(nums, 0, len(nums) - 1))





















        
    
