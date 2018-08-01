class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k == 0:
            return False

        if t == 0 and len(nums) == len(set(nums)):
            return False

        from collections import deque

        d = {}
        l = deque()
        for i, n in enumerate(nums):
            cur_min = n - t
            cur_max = n + t

            for key in d:
                if (d[key] is not None) and cur_min <= key <= cur_max:
                    print(n, key, l, d)
                    return True

            l.append(n)
            if len(l) > k:
                v = l.popleft()
                d[v] = None
            d[n] = i

        return False