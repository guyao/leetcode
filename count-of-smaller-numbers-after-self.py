class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def conquer(nums):
            half = len(nums) // 2
            if half:
                left, right = conquer(nums[:half]), conquer(nums[half:])
                m, n = len(left), len(right)
                i = j = 0
                while i < m or j < n:
                    if j == n or i < m and left[i][1] <= right[j][1]:
                        nums[i+j] = left[i]
                        res[left[i][0]] += j
                        i += 1
                    else:
                        nums[i+j] = right[j]
                        j += 1
            return nums
        res = [0] * len(nums)
        conquer(list(enumerate(nums)))
        return res

nums = [5, 2, 6, 1]
# expect [2, 1, 1, 0]
r = Solution().countSmaller(nums)
print(r)