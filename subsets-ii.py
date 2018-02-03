class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        def dfs(st, path):
            res.append(path[:])
            for i in range(st, len(nums)):
                if i != st and nums[i] == nums[i-1]:
                    continue
                dfs(i + 1, path + [nums[i]])
        dfs(0, [])
        return res