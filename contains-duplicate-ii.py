class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        m = {}
        for i, n in enumerate(nums):
            if n not in m:
                m[n] = i
            else:
                if i - m[n] <= k:
                    return True
                else:
                    m[n] = i
        return False