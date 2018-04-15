# Solution 1
import math
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num < 2:
            if num == 0:
                return [0]
            elif num == 1:
                return [0, 1]
        result = [0, 1]
        u  = math.floor(math.log(num, 2))
        rst = num % 2**u + 1
        for iu in range(2, u + 1):
            result.extend([result[i] + 1 for i in range(2**(iu - 1))])
        result.extend([result[i] + 1 for i in range(rst)])
        return result

# Solution 2
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0 for _ in range(num + 1)]
        for i in range(num + 1):
            result[i] = result[i // 2] + (i&1)
        return result