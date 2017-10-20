class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not any(nums):
            return 0
        INF = float('inf')
        total = 0
        l = INF
        j = 0
        cnt = 0
        sum_list = [0]
        for n in nums:
            cnt += n
            sum_list.append(cnt)
        def sum_range(i, j):
            return sum_list[j] - sum_list[i]

        for i in range(len(nums)):
            total = sum_range(i, j)
            while j < len(nums) and total < s:
                j += 1
                total = sum_range(i, j)
            if total >= s:
                l = min(l, j-i)
        return l if l != INF else 0

t = [2,3,1,2,4,3]
s, t = 11, [1,2,3,4,5]
s, t = 15, [1,2,3,4,5]
s, t = 7, [2,3,1,2,4,3]
s, t = 3, [1,1]
r = Solution().minSubArrayLen(s, t)
print(r)
