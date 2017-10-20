"""
Valid Triangle
A[i] + A[j] > A[k]
A[i] + A[k] > A[j]
A[j] + A[k] > A[i]

if array is sorted, with i < j < k
A[i] < A[j] < A[k]
√ A[k] + A[j] > A[i]
√ A[k] + A[i] > A[j]
? A[i] + A[j] > A[k]
"""
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        for k in reversed(range(2, len(nums))):
            target = nums[k]
            l, r = 0, k - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    count += r - l
                    r -= 1
                else:
                    l += 1
        return count

t = [2, 2, 3, 4]
r = Solution().triangleNumber(t)
