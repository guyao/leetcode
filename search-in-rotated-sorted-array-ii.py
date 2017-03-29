"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = 0
        r = len(nums) - 1
        if nums[l] >= nums[r]:
            pass
            if nums[l] < target:
                while l < r and nums[r] <= nums[l]:
                    r -= 1
                while l < r:
                    # while l == 0 or (l > 0 and nums[l] == nums[l - 1]):
                    #     l += 1
                    m = (l + r) // 2
                    if nums[m] < target:
                        l = m + 1
                    else:
                        r = m
            elif target < nums[r]:
                while l < r and nums[r] <= nums[l]:
                    l += 1
                while l < r:
                    # while r == len(nums) - 1 or (r < len(nums) - 1 and nums[r] == nums[r+1]):
                    #     r -= 1
                    m = (l + r) // 2
                    if nums[m] < target:
                        l = m + 1
                    else:
                        r = m
                    print(l, m, r, ":", nums[l], nums[m], nums[r])
            else:
                if target == nums[l] or target == nums[r]:
                    return True
        else:
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
        return True if nums[r] == target else False

"""
   x
  x
xx   xx
    x
   x

"""
t = [3,4,4,4,4,4,4,5,5,6,6,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,10,10,10,-10,-10,-10,-9,-8,-8,-8,-8,-8,-7,-7,-7,-7,-6,-6,-6,-6,-6,-6,-6,-5,-5,-5,-4,-4,-4,-4,-3,-3,-3,-3,-3,-3,-2,-2,-2,-2,-1,-1,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3]
r = Solution().search(t, 2)
print(r)