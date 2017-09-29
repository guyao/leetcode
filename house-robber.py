"""
State: 
    f[i] = max value of i houses
Function: 
    f[i] = max(f[i-2] + A[i], f[i-1])
Intialization: 
    F[0] = A[0]
    F[1] = max(A[1], A[0])
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        ans = [0 for i in range(len(nums))]
        ans[0] = nums[0]
        ans[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            ans[i] = max(ans[i-2]+nums[i], ans[i-1])
        return ans[-1]

"""
State: 
    f[i] = max value of i houses, i must be robbed
Function: 
    f[i] = max(f[i-2], f[i-3]) + A[i])
Intialization: 
    F[0] = A[0]
    F[1] = A[1]
    F[2] = A[0] + A[2]
Answer:
    max(F)
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        ans = [0 for i in range(len(nums))]
        ans[0] = nums[0]
        ans[1] = nums[1]
        ans[2] = nums[0]+nums[2]
        for i in range(3, len(nums)):
            ans[i] = max(ans[i-3]+nums[i], ans[i-2]+nums[i])
        return max(ans)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for n in nums:
            last, now = now, max(last+n, now)
        return now


nums = [3,6,8,9,2,5,3,7,6,5,1,2,8,6,1,2,6,7]
nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
r = Solution().rob(nums)
print(r)

