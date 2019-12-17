"""
pointer i: valid s[:i]
pointer j: to explore

if meet '#', i -= 1
else, s[i] = s[j]

Edge cases: 
"a##", after deleting a, can not delete more

"""


class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def process(s):
            s = list(s)
            i = 0
            for j in range(len(s)):
                if s[j] == "#":
                    i -= 1
                    if i < 0: i = 0
                    continue
                if i != j: s[i] = s[j]
                i += 1
            return "".join(s[:i])

        return process(S) == process(T)