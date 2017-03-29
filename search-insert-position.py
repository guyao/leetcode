"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while r - l > 1:
            m = (l + r) // 2
            if target < nums[m]:
                if nums[m - 1] < target:
                    r = m
                    return m
                else:
                    r = m - 1
            elif target > nums[m]:
                if nums[m + 1] > target:
                    l = m
                    return m + 1
                else:
                    l = m + 1
            else:
                return m

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r + 1) // 2
            if target < nums[m]:
                r = m - 1
            else:
                l = m
        return l+1 if nums[l] < target else l


t = [1,3,5,6]

f = lambda x: Solution().searchInsert(t, x)




