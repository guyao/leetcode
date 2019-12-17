class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = []
        s = []
        for i in reversed(range(len(temperatures))):
            while s and temperatures[s[-1]] <= temperatures[i]:
                s.pop()
            res.append(s[-1] - i if s else 0)
            s.append(i)
        res.reverse()
        return res