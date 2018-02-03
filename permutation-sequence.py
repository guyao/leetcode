class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
        def permutate(candidates, n, k):
            if n == 1:
                return candidates
            num = factorial(n - 1)
            idx = k // num
            cur = candidates[idx]
            candidates = candidates[:idx] + candidates[idx + 1:]
            return [cur] + permutate(candidates, n - 1, k % num)
        candidates = list(range(1, n + 1))
        return "".join([str(i) for i in permutate(candidates, n, k - 1)])