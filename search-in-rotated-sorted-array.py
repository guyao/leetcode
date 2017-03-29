"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2
        while l < r:
            print("*"*20)
            print(l, m, r)
            m = (l + r) // 2
            if nums[l] > nums[r]:
                if nums[m] >= nums[l]:
                    if nums[m] < target:
                        l = m + 1
                    elif nums[m] > target:
                        r = m - 1
                    else:
                        return m
                elif nums[m] <= nums[r]:
                    if target < nums[m]:
                        r = m - 1
                    elif nums[m] < target:
                        l = m + 1
                    else:
                        return m
            else:
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            print(l, m, r)
            print("*"*20)

        return r if nums[r] == target else -1

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2
        while l < r:
            if nums[l] > nums[r]:
                if target >= nums[l]:
                    while nums[r] < nums[l]:
                        r -= 1
                    while l < r:
                        m = (l + r) // 2
                        if nums[m] < target:
                            l = m + 1
                        else:
                            r = m
                elif target <= nums[r]:
                    while nums[l] > nums[r]:
                        l += 1
                    while l < r:
                        m = (l + r) // 2
                        if nums[m] < target:
                            l = m + 1
                        else:
                            r = m
                else:
                    return -1
            else:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
        return r if len(nums) != 0 and nums[r] == target else -1

t = [3, 4, 5, 6, 1, 2]
# t = [1]
# t = [1, 3]
t = [3, 1]
r = Solution().search(t, 2)
print(r)
