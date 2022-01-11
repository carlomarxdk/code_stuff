def contains_duplicate(nums: List[int]) -> bool:
    """
    :rtype: bool
    """
    unique = set(nums)
    if len(unique) == len(nums):
        return False
    else:
        return True