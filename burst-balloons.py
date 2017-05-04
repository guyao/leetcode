"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

"""

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        dp = [[None]*len(nums) for _ in range(len(nums))]
        def calc(lo, hi):
            if dp[lo][hi] is not None:
                return dp[lo][hi]
            s = 0
            for i in range(lo+1, hi):
                s = max(
                    s,
                    nums[lo]*nums[i]*nums[hi] + calc(lo, i) + calc(i, hi)
                    )
            dp[lo][hi] = s
            return s


        r = calc(0, len(nums)-1)
        return r

t = [3, 1, 5, 8]
# expect = 167
"""
 nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""
r = Solution().maxCoins(t)