# https://leetcode.com/problems/largest-number

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = [str(n) for n in nums]
        def f(x, y):
            return 1 if x + y < y + x else -1

        def cmp_to_key(mycmp):
            'Convert a f= function into a key= function'
            class K:
                def __init__(self, obj, *args):
                    self.obj = obj
                def __lt__(self, other):
                    return mycmp(self.obj, other.obj) < 0
                def __gt__(self, other):
                    return mycmp(self.obj, other.obj) > 0
                def __eq__(self, other):
                    return mycmp(self.obj, other.obj) == 0
                def __le__(self, other):
                    return mycmp(self.obj, other.obj) <= 0
                def __ge__(self, other):
                    return mycmp(self.obj, other.obj) >= 0
                def __ne__(self, other):
                    return mycmp(self.obj, other.obj) != 0
            return K
        nums = sorted(nums, key=cmp_to_key(f))
        return "".join(nums).lstrip("0") or "0"