class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if all([len(w) == 1 for w in wall]): return len(wall)
        import heapq
        import collections
        
        def poppush():
            v, i = heapq.heappop(heap)
            i, j = i
            if j + 1 < len(wall[i]):
                if wall[i][j+1] + v < sum(wall[0]):
                    heapq.heappush(heap, (wall[i][j+1] + v, (i, j + 1)))
            return v

        heap = []
        
        for i, w in enumerate(wall):
            v = (w[0], (i, 0))
            heapq.heappush(heap, v)
        
        def f():
            while heap: yield poppush()
        mx = max(collections.Counter(list(f())).values())
        return len(wall) - mx

# Edge Cases
# [[1], [1], [1]] expect 3
# [[1,1], [1,1], [1,1]] expect 0