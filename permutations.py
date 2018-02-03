# https://leetcode.com/problems/permutations

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited = set()
        res = []
        def dfs(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for n in nums:
                if n not in visited:
                    visited.add(n)
                    dfs(path + [n])
                    visited.remove(n)
        dfs([])
        return res

