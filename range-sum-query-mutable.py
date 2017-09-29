#Segment Tree
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        from math import log
        self.len = len(nums)
        self.nums = nums

        height = int(log(len(nums), 2)) + 1 if len(nums) != 0 else 1
        self.st = [0] * (2**(height+1) - 1)

        def constructUtil(l, r, i):
            if l > r:
                return
            if l == r:
                self.st[i] = nums[l]
                return nums[l]
            m = (l+r) // 2
            self.st[i] = constructUtil(l, m, 2*i+1) + constructUtil(m+1, r, 2*i+2)
            return self.st[i]
        constructUtil(0, len(nums)-1, 0)


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        def updateUtil(l, r, index, i, diff):
            if index < l or index > r:
                return
            self.st[i] += diff
            m = (l+r) // 2
            if l != r:
                updateUtil(l, m, index, 2*i+1, diff)
                updateUtil(m+1, r, index, 2*i+2, diff)
        updateUtil(0, self.len - 1, i ,0, diff)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def sumUtil(l, r, ql, qr, i):
            if ql <= l and qr >= r:
                return self.st[i]
            if qr < l or ql > r:
                return 0
            m = (l+r) // 2
            return sumUtil(l, m, ql, qr, 2*i+1) + sumUtil(m+1, r, ql, qr, 2*i+2)
        return sumUtil(0, self.len - 1, i, j, 0)

#Binary Indexed Tree        
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.len = len(nums)
        self.bit = [0] * (len(nums)+1)
        for i in range(len(nums)):
            self.update_bit(i, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        self.update_bit(i, diff)

    def update_bit(self, i, diff):
        i = i + 1
        while i <= self.len:
            self.bit[i] += diff
            i = i + (i&(-i))

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def getsum(idx):
            idx = idx + 1
            s = 0
            while idx > 0:
                s += self.bit[idx]
                idx = idx - (idx&(-idx))
            return s
        return getsum(j) - getsum(i-1) if i != 0 else getsum(j)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

nums = [3,4,1,7,4,5,2,9,4,3,1,9]
# nums = []
obj = NumArray(nums)






