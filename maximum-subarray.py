"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

# O(n) runtime, O(1) space DP
"""
f(k) max sum of subarray ending at index k
f(k) = max(f(k-1)+A[k], A[k])

1. State
  local[i] max value if contains x[i]
  global[i] global value at index i
2. Function
  local[i] = Max(nums[i], local[i-1]+nums[i])
  global[i] = Max(local[i], global[i-1])
3. Intialization
  local[0] = global[0] = nums[0]
4. Answer
  global[i-1]
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSumHere = 0
        maxSumSoFar = 0
        for i in nums:
            maxSumHere = max(maxSumHere + i, i)
            maxSumSoFar = max(maxSumSoFar, maxSumHere)
        return maxSumSoFar

#Divide and Conquer
"""

Assume we partition the array A into two smaller arrays S and T at the
middle index, M. Then, S = A 1 … A M-1 , and T = A M+1 … A N . The
contiguous subarray that has the largest sum could either: 
i. Contain the middle element:     
    a. The largest sum is the maximum suffix sum of S + A M + the maximum 
    prefix sum of T. 
ii. Does not contain the middle element:     
    a. The largest sum is in S, which we could apply the same algorithm to S.
    b. The largest sum is in T, which we could apply the same algorithm to T.

"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.conquer(nums, 0, len(nums) - 1)

    def conquer(self, nums, i, j):
        if i > j:
            return -float('inf')
        m = (i + j) // 2
        lmaxsum = self.conquer(nums, i, m - 1)
        rmaxsum = self.conquer(nums, m + 1, j)
        prefixsum = 0
        maxprefixsum = 0
        for i1 in reversed(range(i, m)):
            prefixsum = prefixsum + nums[i1]
            maxprefixsum = max(maxprefixsum, prefixsum)
        suffixsum = 0
        maxsuffixsum = 0
        for i2 in range(m+1, j+1):
            suffixsum = suffixsum + nums[i2]
            maxsuffixsum = max(maxsuffixsum, suffixsum)
        s = max(maxsuffixsum + nums[m] + maxprefixsum, lmaxsum, rmaxsum)
        return s

t = [2, 1, -3, 4, -1, 2, 1, -5, 4]
r = Solution().maxSubArray(t)



