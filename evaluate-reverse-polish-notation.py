# https://leetcode.com/problems/evaluate-reverse-polish-notation
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        OPERATORS = ["+", "-", "*", "/"]
        def calc(a, b, op):
            if op == "+":
                return a + b
            elif op == "-":
                return a - b
            elif op == "*":
                return a * b
            elif op == "/":
                res = abs(a) // abs(b)
                return -res if a * b < 0 else res
            else:
                pass
        evaluate = []
        for c in tokens:
            if c in OPERATORS:
                b = evaluate.pop()
                a = evaluate.pop()
                result = calc(a, b, c)
                evaluate.append(result)
            else:
                evaluate.append(int(c))
        return evaluate[-1]