def threeSum(nums):
        idx_map, res = {}, []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                key = -1 * (nums[i] + nums[j])
                if (key in idx_map) and (i != idx_map[key]) and (j != idx_map[key]):
                    res.append((nums[i], nums[j], key)
                else:
                    idx_map[nums[j]] = j
        return res
