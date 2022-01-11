def maxArea(self, height: List[int]):
    """
    :rtype: int
    """
    l_indx = 0
    r_indx = len(height) - 1
    area = 0
    while l_indx < r_indx:
        area = max(area, (r_indx - l_indx) * min(height[l_indx], height[r_indx]))
        if height[l_indx] > height[r_indx]:
            r_indx -= 1
        else:
            l_indx += 1
    return area
                