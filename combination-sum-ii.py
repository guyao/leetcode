"""
Combination Sum II
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()

        def dfs(candidates, st, target, path):
            if target < 0:
                return
            if target == 0:
                result.append(path)
            for i in range(st, len(candidates)):
                if i != st and candidates[i] == candidates[i - 1]:
                    continue
                dfs(candidates, i + 1, target -
                    candidates[i], path + [candidates[i]])
        dfs(candidates, 0, target, [])
        return result


t = [10, 1, 2, 7, 6, 1, 5]
r = Solution().combinationSum2(t, 8)
print(r)
