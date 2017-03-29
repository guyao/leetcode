"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        water = 0
        level = 0
        while l < r:
            if height[l] < height[r]:
                lower = height[l]
                l += 1
            else:
                lower = height[r]
                r -= 1
            if lower > level:
                level = lower
            water += level - lower
        return water


t = [0,1,0,2,1,0,1,3,2,1,2,1]
t = [0]
t = [1, 2, 3]
t = [1]
t = [5,4,1,2]
t = [5,2,1,2,1,5] # 14
r = Solution().trap(t)
print(r)
