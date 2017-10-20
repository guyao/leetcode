class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo = [[None]*len(nums) for i in range(len(nums))]
        def helper(l, r):
            if l == r:
                return nums[l]
            else:
                if not memo[l][r]:
                    memo[l][r] = max(
                        nums[l] - helper(l+1, r),
                        nums[r] - helper(l, r-1)
                        )
                return memo[l][r]
        return helper(0, len(nums)-1) >= 0

t = [1, 5, 2]
t = [1, 5, 233, 7]
t = [0]
t = [1, 1]
t = [2,4,55,6,8]
r = Solution().PredictTheWinner(t)
print(r)



