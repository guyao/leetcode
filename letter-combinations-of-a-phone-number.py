class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_letter_map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        if digits == "":
            return []
        import functools
        f = lambda acc, digit: [x + y for x in acc for y in num_letter_map[digit]]
        return functools.reduce(f, digits,[''])

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        num_letter_map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        pass
        r = []
        for digit in digits:
            r.append(num_letter_map[digit])
        t = ['']
        for ri in r:
            t = t*len(ri)
            times = int(len(t) / len(ri))
            for j in range(times):
                for i, v in enumerate(ri):
                    t[times*i + j] += v
        return t








Solution().letterCombinations("23")