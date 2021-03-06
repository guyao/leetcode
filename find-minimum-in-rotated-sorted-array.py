"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            m = (l + r) // 2
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m
        return nums[l]




t = [4, 5, 6, 7, 0, 1, 2]
t = [2, 1]
r = Solution().findMin(t)
