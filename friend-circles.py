class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        l = len(M)
        uf = [i for i in range(l)]
        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                uf[px] = py

        def find(x):
            # compressed find
            p = parent(x)
            while p != parent(p):
                p = parent(p)
            result = p
            temp = -1
            cur = x
            while cur != parent(cur):
                temp = parent(cur)
                if uf[cur] != result:
                    uf[cur] = result
                cur = temp
            return result

        def parent(x):
            return uf[x]
        for i in range(len(M)):
            for j in range(i, len(M[0])):
                if M[i][j] == 1:
                    union(i, j)
        big_father = [i for i in range(l)]
        for i, v in enumerate(uf):
            big_father[i] = find(i)
        return len(set(big_father))




t = [[1,1,0],
 [1,1,0],
 [0,0,1]]
t = [[1,1,0],
 [1,1,1],
 [0,1,1]]
t = [[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]

r = Solution().findCircleNum(t)
print(r)

