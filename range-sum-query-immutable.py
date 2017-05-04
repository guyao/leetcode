class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = []
        s = 0
        for n in nums:
            s += n
            self.sums.append(s)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j] if i == 0 else self.sums[j] - self.sums[i-1]
        


nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
r = obj.sumRange(2, 5)
print(r)