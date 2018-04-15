from heapq import heapify, heappop
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = Counter(nums)
        x = [(-c[key], key) for key in c]
        heapify(x)
        if k <= len(nums):
            return [heappop(x)[1] for _ in range(k)]