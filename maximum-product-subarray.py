"""
Find the contiguous subarray within an array (containing at least one number)
which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxans = nums[0]
        maxhere = nums[0]
        minhere = nums[0]
        for i in nums[1:]:
            mx = maxhere
            mn = minhere
            maxhere = max(mx * i, i, mn * i)
            minhere = min(mn * i, i, mx * i)
            maxans = max(maxans, maxhere)
        return maxans


t1 = [2, 3, -3, 4] # expect 6([2, 3])
t2 = [-4,-3,-2]
t3 = [-1, 0, -1]
