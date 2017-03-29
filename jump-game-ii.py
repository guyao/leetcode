"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""

# Time Exceed
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = []
        r.append(float('inf'))
        step = nums[0]
        if len(nums) == 1:
            return 0
        if nums[0] == 0:
             return float('inf')
        if nums[0] >= len(nums) - 1:
            return 1
        for i in range(1, 1+step):
            if i < len(nums):
                r.append(1 + self.jump(nums[i:]))
        ret = min(r)
        return ret if ret != float('inf') else float('inf')

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        start = 0
        maxend = 0
        step = 0
        if start != n and start + nums[start] >= n:
            return 1
        while start < n:
            step += 1
            for i in range(start + 1, nums[start] + start + 1):
                if i + nums[i] >= n:
                    return step + 1
                if i + nums[i] > maxend:
                    maxend = i + nums[i]
                    start = i
        return step


t = [2,3,1,1,4]
t = [0]
t = [2,9,6,5,7,0,7,2,7,9,3,2,2,5,7,8,1,6,6,6,3,5,2,2,6,3]
t = [8,4,3,4,0,0,9,7,2,3,5,7,3,1,1,5,1,8,6,1,1,6,1,1,8,0,4]
t = [2,1]
r = Solution().jump(t)