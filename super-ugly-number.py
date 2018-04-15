# Time Limit Exceed
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ns = [0 for _ in primes]
        result = [1]
        count = 1
        while count < n:
            values = {p * result[num]:i for (i, (num,p)) in enumerate(zip(ns, primes))}
            if result[-1] != min(values):
                result.append(min(values))
                count += 1
            idx = values[min(values)]
            ns[idx] += 1
        return result[-1]


n = 100000
primes = [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]