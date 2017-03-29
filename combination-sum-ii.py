"""
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

#Time Exceeded
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        r = self.helper(candidates, target)
        s = set()
        for i in r:
            s.add(tuple(i))
        return [list(i) for i in s]

    def helper(self, candidates, target):
        if target < 0:
            return []
        candidates = sorted(candidates)
        result = []
        for i, v in enumerate(candidates):
            if target == v:
                result.append([v])
            r = self.helper(candidates[i+1:], target - v)
            for item in r:
                result.append([v] + item)
        return result

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        r = self.helper(candidates, target)
        return r

    def helper(self, candidates, target):
        if target < 0:
            return []
        result = []
        for i, v in enumerate(candidates):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            if target == v:
                result.append([v])
            r = self.helper(candidates[i+1:], target - v)
            for item in r:
                result.append([v] + item)
        return result
        

t = [10, 1, 2, 7, 6, 1, 5]
r = Solution().combinationSum2(t, 8)