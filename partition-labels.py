from functools import lru_cache

class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        @lru_cache(None)
        def dfs(s):
            mx = 1
            idx = [len(s)]
            for i in range(1, len(s)):
                if not set(s[:i]) & set(s[i:]):
                    newmx, newidx = dfs(s[i:])
                    if 1 + newmx > mx:
                        mx = newmx + 1
                        idx = [i] + newidx
            return mx, idx
        mx, splits = dfs(S)
        return splits