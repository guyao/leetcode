class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binary_search_and_insert(nums, k):
            if not nums or nums[-1] < k:
                nums.append(k)
            l = 0
            r = len(nums) - 1
            while l < r:
                m = (l + r) // 2
                if nums[m] < k:
                    l = m + 1
                else:
                    r = m
            nums[l] = k

        monotonic_stack = []

        for n in nums:
            binary_search_and_insert(monotonic_stack, n)

        return len(monotonic_stack)

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)
        