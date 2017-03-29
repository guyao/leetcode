"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
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
            m = (l + r) // 2
            if nums[r] < nums[m]:
                l = m + 1
            elif nums[r] > nums[m]:
                r = m
            else:
                r -= 1
        return nums[l]

t = [2, 4, 5, 6, 7, 0, 1, 2, 2]
t = [10,1,10,10,10]
r = Solution().findMin(t)
