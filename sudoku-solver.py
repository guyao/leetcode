class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.ans = None
        self.dfs(board, 0)


    def dfs(self, board, pos):
        if pos >= 81:
            return True
        x = pos // 9
        y = pos % 9
        if board[x][y] != ".":
            return self.dfs(board, pos + 1)
        else:
            basic = set("1234566789")
            a = set()
            b = set()
            c = set()
            for i in range(9):
                if board[x][i] != ".":
                    a.add(board[x][i])
            for i in range(9):
                if board[i][y] != ".":
                    b.add(board[i][y])
            block_x = x//3*3
            block_y = y//3*3
            for i in range(block_x, block_x+3):
                for j in range(block_y, block_y+3):
                    c.add(board[i][j])
            a = basic.difference(a)
            b = basic.difference(b)
            c = basic.difference(c)
            candidates = (a.intersection(b)).intersection(c)
            for c in candidates:
                row = list(board[x])
                row[y] = c
                board[x] = ''.join(row)
                if self.dfs(board, pos + 1):
                    return True
                else:
                    row = list(board[x])
                    row[y] = "."
                    board[x] = ''.join(row)

t = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
t = [
    "53..7....",
    "6..195...",
    ".98....6.",
    "8...6...3",
    "4..8.3..1",
    "7...2...6",
    ".6....28.",
    "...419..5",
    "....8..79"
    ]

r = Solution().solveSudoku(t)
print(t)