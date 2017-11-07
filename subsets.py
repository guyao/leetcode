# https://leetcode.com/problems/subsets/description/
# DFS
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def dfs(index, path, res):
            res.append(path)
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]], res)
        dfs(0, [], res)
        return res

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in sorted(nums):
            res += [item + [num] for item in res]
        return res

Solution().subsets([1, 2, 3])
