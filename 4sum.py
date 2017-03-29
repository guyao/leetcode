"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class ListNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        self.results = []
        self.findSum(nums, target, 4, [])
        return self.results

    def findSum(self, nums, target, N, result):
        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    self.results.append(result+[nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(len(nums) - (N - 1)):
                if i == 0 or i > 0 and nums[i-1] != nums[i]:
                    self.findSum(nums[i+1:], target - nums[i], N - 1, result + [nums[i]])


t = [1, 0, -1, 0, -2, 2]
r = Solution().fourSum(t, 0)