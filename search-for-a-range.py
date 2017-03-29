"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        left = l if nums[l] == target else -1
        r = len(nums) - 1
        while l < r:
            m = (l + r + 1) // 2
            if target < nums[m]:
                r = m - 1
            else:
                l = m
        right = l if nums[r] == target else -1
        return [left, right]

t = [5, 7, 7, 8, 8, 10]
r = Solution().searchRange(t, 8)