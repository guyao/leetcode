"""
Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
Subscribe to see which companies asked this question.

Show Tags
Show Similar Problems

"""
class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """

        memo = {}
        nums = [i for i in range(1, maxChoosableInteger+1)]
        if sum(nums) < desiredTotal:
            return False
        print(nums)
        def make_hashable(nums):
            return str(nums)
        def helper(nums, desired):
            hash = make_hashable(nums)
            if hash in memo:
                return memo[hash]
            if nums[-1] >= desired:
                return True
            for i, n in enumerate(nums):
                if not helper(nums[:i] + nums[i+1:], desired - n):
                    memo[hash] = True
                    return True
            memo[hash] = False
            return False
        return helper(nums, desiredTotal)

