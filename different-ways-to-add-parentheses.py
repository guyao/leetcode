class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        import re
        import operator
        tokens = re.split('(\D)', input)
        nums = [int(i) for i in tokens[::2]]
        ops = [{'+': operator.add, '-': operator.sub, '*': operator.mul}.get(i) for i in tokens[1::2]]
        def build(lo, hi):
            res = []
            if lo == hi:
                return [nums[lo]]
            for i in range(lo, hi):
                for a in build(lo, i):
                    for b in build(i+1, hi):
                        res.append(ops[i](a,b))
            return res
        return build(0,len(nums)-1)

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        import re
        import operator
        tokens = re.split('(\D)', input)
        nums = list(map(int, tokens[::2]))
        ops = list(map({
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul
            }.get, tokens[1::2]))
        def build(lo, hi):
            if lo == hi:
                return [nums[lo]]
            return [ops[i](a,b)
                for i in range(lo, hi)
                for a in build(lo, i)
                for b in build(i+1, hi)
            ]
        return build(0, len(nums)-1)



t = "2-1-1"
r = Solution().diffWaysToCompute(t)


