def two_sum(self, nums: List[int], target: int) -> List[int]:
    diff = {}
    for i in range(len(nums)):
        if nums[i] in diff.keys():
            return [diff[nums[i]], i]
        else:
            diff[target - nums[i]] = i
    return [None, None]