"""
Given an array S of n integers,
are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r = []
        if len(nums) < 3:
            return r
        end = len(nums) - 1
        numlist = sorted(nums)
        for i, v in enumerate(numlist):
            if (i > 0) and numlist[i] == numlist[i - 1]:
                continue
            if i + 1 < end:
                other = self.twoSum(numlist, -v, i + 1, end)
                for ans in other:
                    r.append([v] + ans)
        return r

    def twoSum(self, nums, key, start, end):
        p = start
        q = end
        r = []
        lastp = nums[start]
        lastq = nums[end]
        while p < q:
            if (p > start) and (nums[p] == lastp):
                p += 1
                continue
            if (q < end) and (nums[q] == lastq):
                q -= 1
                continue
            s = nums[p] + nums[q]
            print("p", key, s)
            if s < key:
                p += 1
            elif s > key:
                q -= 1
            else:
                r.append([nums[p], nums[q]])
                lastp = nums[p]
                lastq = nums[q]
                p += 1
                q -= 1
        return r


S = [-1, 0, 1, 2, -1, -4]  # expected [[-1, 0, 1], [-1, -1, 2]]
S2 = [-2, 0, 0, 2, 2]  # expected [[-2, 0, 2]]
S3 = [0, 0, 0]  # expect [[0, 0, 0]]
S4 = [-1, 0, 1, 2, -1, -4]  # expect [[-1,-1,2],[-1,0,1]]
S5 = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
S6 = [-1, 0, 1]
S7 = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
S8 = [0, -4, -1, -4, -2, -3, 2]
# expect [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
