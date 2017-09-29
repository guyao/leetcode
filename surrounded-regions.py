"""
Union Find
"regions surrounded by 'X'" == whether region could connect to outside
surround board with O
"""
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        INF = 0
        if not any(board):
            return
        def find(x):
            p = uf[x]
            while p != uf[p]:
                p = uf[p]
            result = p
            t = -1
            p = x
            while p != uf[p]:
                t = uf[p]
                uf[p] = result
                p = t
            return result
        def union(x, y):
            p_x = find(x)
            p_y = find(y)
            if p_x != p_y:
                p_x, p_y = (p_x, p_y) if p_x < p_y else (p_y, p_x)
                uf[p_y] = p_x
        def index(x, y):
            return x*wd + y
        def search(x, y):
            for i_x, i_y in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
                if mp[i_x][i_y] == "O":
                    union((index(x, y)), (index(i_x, i_y)))

        ht = len(board)
        wd = len(board[0])
        mp = [["O"]*(wd+2)] + [["O"] + list(l) + ["O"] for l in board] + [["O"]*(wd+2)]
        ht = len(mp)
        wd = len(mp[0])
        uf = [i for i in range(ht*wd)]
        for i in [0, ht-1]:
            for j in range(wd):
                idx = index(i, j)
                uf[idx] = INF
        for j in [0, wd-1]:
            for i in range(ht):
                idx = index(i, j)
                uf[idx] = INF
        for i in range(1, ht-1):
            for j in range(1, wd-1):
                if mp[i][j] == "O":
                    search(i, j)

        for i in range(ht):
            for j in range(wd):
                if mp[i][j] == "O":
                    find(index(i, j))

        for i in range(ht):
            for j in range(wd):
                if mp[i][j] == "O":
                    if uf[index(i, j)] != INF:
                        mp[i][j] = "X"

        mp = [''.join(l) for l in mp]
        board[:] = [l[1:wd-1] for l in mp[1:ht-1]]

t = ["XXXX","XOOX","XXOX","XOXX"]
t = ["XOXX","OXOX","XOXO","OXOX","XOXO","OXOX"]
Solution().solve(t)
