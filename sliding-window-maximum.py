class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not any(nums):
            return []
        from collections import deque
        q = deque()

        def insert(i, x):
            if q:
                end, end_v = q[-1]
                while end_v < x:
                    q.pop()
                    if q:
                        end, end_v = q[-1]
                    else:
                        break
            q.append((i, x))
        def valid(i):
            if q:
                front, front_v = q[0]
                while front < i - k + 1:
                    q.popleft()
                    if q:
                        front, front_v = q[0]
                    else:
                        break
        result = []

        for i in range(k-1):
            insert(i, nums[i])
            valid(i)

        for i in range(k-1, len(nums)):
            insert(i, nums[i])
            valid(i)
            result.append(q[0][1])
        return result

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        dq = deque()
        max_nums = []
        for i in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            while i >= k-1 and dq[0] <= i - k:
                dq.popleft()
            if i >= k - 1:
                max_nums.append(nums[dq[0]])
        return max_nums

t, k = [1,3,-1,-3,5,3,6,7], 3
t, k = [1, -1], 1 #expect [1, -1]
# t, k = [1,3,1,2,0,5], 3

r = Solution().maxSlidingWindow(t, k)
print(r)