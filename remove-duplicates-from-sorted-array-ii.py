class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        FREQUENCY = 2
        idx = -1
        count = 0
        for i in range(len(nums)):
            if nums[i] != nums[idx]:
                count = 1
                idx += 1
                nums[idx] = nums[i]
            else:
                count += 1
                if count <= FREQUENCY:
                    idx += 1
                    nums[idx] = nums[i]
        return idx + 1