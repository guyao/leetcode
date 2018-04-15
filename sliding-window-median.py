class Solution:
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        import bisect
        nums = nums + [0]
        result = []
        window = sorted(nums[:k])
        for i in range(k, len(nums)):
            median = (window[k//2] + window[(k-1)//2]) / 2
            result.append(median)
            window.pop(bisect.bisect_left(window, nums[i - k]))
            bisect.insort(window, nums[i])
        return result
        

