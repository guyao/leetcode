"""
f(k) = max(f(k-2)+nums[k], f(k-1))
f(1) = max(nums[0], nums[1])
f(0) = nums[0]
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for n in nums:
            last, now = now, max(last+n, now)
        return now

nums = [3,6,8,9,2,5,3,7,6,5,1,2,8,6,1,2,6,7]
nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
r = Solution().rob(nums)
print(r)

