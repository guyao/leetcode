class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        from heapq import heappush, heappop, heappushpop
        max_heap, min_heap = [], []

        def insert(n):
            heappush(max_heap, -heappushpop(min_heap, n))
            if len(max_heap) > len(min_heap):
                heappush(min_heap, -heappop(max_heap))

        def median():
            if len(min_heap) > len(max_heap):
                return min_heap[0]
            else:
                return (min_heap[0] - max_heap[0]) / 2.0

        for i in range(k-1):
            insert(nums[i])
        for i in range(k-1,len(nums)):
            insert(nums[i])
            print(median())

        return None
        
t = [1, 3, -1, -3, 5, 3, 6, 7]
r = Solution().medianSlidingWindow(t, 3)
print(r)
