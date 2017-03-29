"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        k = -1
        for i in reversed(range(len(nums) - 1)):
            if not nums[i] >= nums[i+1]:
                k = i
                break
        if k == -1:
            nums[:] = sorted(nums)
            return
        for i in reversed(range(k + 1, len(nums))):
            if nums[i] > nums[k]:
                nums[k], nums[i] = nums[i], nums[k]
                break
        nums[k+1:] = sorted(nums[k+1:])

t = [5, 1, 1] # expect [1, 1, 5]
t = [1, 5, 1] # expect [1, 1, 5]
Solution().nextPermutation(t)
print(t)



