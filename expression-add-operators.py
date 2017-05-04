class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        def helper(num, path, val, multed):
            # print(num, path, val)
            if num == "":
                if target == val:
                    res.append(path)
            for i in range(1, len(num)+1):
                n = int(num[:i])
                # if str(int(num[:i])) != num[:i]:
                    # break
                if i != 1 and num[:i][0] == "0":
                    break
                if path == "":
                    helper(num[i:], path + num[:i], n, n)
                else:
                    helper(num[i:], path + "+" + num[:i], val + n, n)
                    helper(num[i:], path + "-" + num[:i], val - n, -n)
                    helper(num[i:], path + "*" + num[:i], val - multed + multed * n, multed * n)
        helper(num, "", 0, 0)
        return res



num = "105"
target = 5
#expect ["1*0+5", "10-5"]

r = Solution().addOperators(num, target)
print(r)

