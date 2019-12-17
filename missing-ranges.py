class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        def build_range(i, j):
            if i == j: return str(i)
            else: return str(i) + "->" + str(j)
        
        nums = [lower - 1] + nums + [upper + 1]
        res = []

        for i in range(len(nums)):
            if i == 0: continue
            if nums[i] - nums[i-1] > 1:
                res.append(build_range(nums[i-1] + 1, nums[i] - 1))

        return res