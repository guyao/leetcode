class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        for i, n in enumerate(nums):
            if nums[i] != nums[idx]:
                idx += 1
                nums[idx] = nums[i]
        return idx + 1