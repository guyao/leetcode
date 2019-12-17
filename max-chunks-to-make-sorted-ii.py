class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        INF = float('inf')
        cur_min = INF
        smaller = []
        for n in reversed(arr):
            if n < cur_min:
                cur_min = n
            smaller.append(cur_min)
        smaller.reverse()

        larger = []
        cur_max = -INF
        for n in arr:
            if n > cur_max:
                cur_max = n
            larger.append(cur_max)

        count = 0
        for i in range(1, len(arr)):
            if smaller[i] >= larger[i - 1]:
                count += 1

        return count + 1