# Solution 1: Counter Sort
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        from collections import Counter
        c = Counter(nums)
        i = 0
        for k in sorted(c.keys()):
            for _ in range(c[k]):
                nums[i] = k
                i += 1

# Solution 2: Rainbow Sort
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def partition(nums, st, ed, k):
            l, r = st, ed - 1
            while l < r:
                while l < r and nums[l] <= k:
                    l += 1
                while l < r and k < nums[r]:
                    r -= 1
                if l < r:
                    nums[l], nums[r] = nums[r], nums[l]
            return l
        st = 0
        ed = len(nums)
        for color in [0, 1, 2]:
            st = partition(nums, st, ed, color)


nums = [1,1,1,2,2,2,2,1,1,1,0,0,0,2,1,0]
Solution().sortColors(nums)