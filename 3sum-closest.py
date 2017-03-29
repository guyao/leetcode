"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        offset = float('inf')
        nums = sorted(nums)
        length = len(nums)
        result = sum(nums[:3])
        for i, vi in enumerate(nums):
            p = i + 1
            q = length - 1
            key = target - vi
            while p < q:
                s = nums[p] + nums[q]
                off = abs(target - (nums[p] + nums[q] + vi))
                if s > key:
                    q -= 1
                else:
                    p += 1
                if off < offset:
                    offset = off
                    result = s + vi
        return result


t = [-1, 2, 1, -4]
# t = [0, 1, 2]
r = Solution().threeSumClosest(t, 1)



                



