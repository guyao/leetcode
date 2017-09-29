"""
sums[0, i] and sums[0, j] => sums[i, j]
hashmap cache the result
sums[0, j] - sums[0, i-1] = sums[i, j]

sum so far, current value
    if "sum so far" - k in hashmap:
        result += map[sum - k]
    count[sum so far ] += 1
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        sums = defaultdict(int)
        s = 0
        cnt = 0
        for i, n in enumerate(nums):
            s += n
            need = s - k
            if need in sums:
                cnt += sums[need]
            if s == k:
                cnt += 1
            sums[s] += 1
        return cnt
