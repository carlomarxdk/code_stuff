def max_subarray(nums: List[int]) -> int:
    """
    Find a subarray that provides the largest sum
    :rtype: int
    """
    if len(nums) == 1:
        return nums[0]
    largest = nums[0]
    total = largest
    for i in range(1, len(nums)):
        current = total + nums[i]
        total = max(current, nums[i])
        largest = max(total, largest)
    return largest