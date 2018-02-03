# https://leetcode.com/problems/permutations-ii
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(candidates, path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(candidates)):
                if i != 0 and candidates[i] == candidates[i-1]:
                    continue
                else:
                    dfs(candidates[:i] + candidates[i+1:], path + [candidates[i]])
                    # print(candidates[:i] + candidates[i+1:], path + [candidates[i]])

        dfs(sorted(nums), [])
        return res