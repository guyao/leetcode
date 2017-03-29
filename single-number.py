"""
Given an array of integers, every element appears twice except for one. Find that single one.


"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in nums:
            result = result ^ i
        return result

t = [1, 1, 2, 2, 3]
r = Solution().singleNumber(t)