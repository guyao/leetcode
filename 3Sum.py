"""
Given an array S of n integers,
are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

"""
Note:
1. avoid duplicate
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        def twosum(nums, st, ed, target):
            l = st
            r = ed
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif s < target:
                    l += 1
                elif s > target:
                    r -= 1

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            n = nums[i]
            twosum(nums, i + 1, len(nums) - 1, -n)
        return res


