"""
max (Assume i included, i excluded)
the solution chose i = n
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        def calc(nums, lo, hi):
            last, now = 0, 0
            for i in range(lo, hi+1):
                last, now = now, max(last+nums[i], now)
            return now
        return max(calc(nums, 0, len(nums)-2), calc(nums, 1, len(nums)-1))

nums = [100, 2, 3, 100]
nums = [1]
r = Solution().rob(nums)
print(r)

        