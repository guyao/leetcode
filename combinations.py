class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []

        def helper(index, path, ct):
            if ct == k:
                res.append(path)
                return
            for i in range(index, n + 1):
                helper(i + 1, path + [i], ct + 1)
        helper(1, [], 0)
        return res


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n:
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1
        return ans
