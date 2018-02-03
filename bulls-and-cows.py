# https://leetcode.com/problems/bulls-and-cows
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        from collections import defaultdict
        secret_counter = defaultdict(int)
        guess_counter = defaultdict(int)
        keys = set()
        bulls = 0
        cows = 0
        l = len(secret)
        for i in range(l):
            s = secret[i]
            g = guess[i]
            if s == g:
                bulls += 1
            else:
                keys.add(s)
                keys.add(g)
                secret_counter[s] += 1
                guess_counter[g] += 1
        for k in keys:
            cows += min(guess_counter[k], secret_counter[k])
        return (str(bulls) + "A" + str(cows) + "B")