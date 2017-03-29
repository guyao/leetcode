#Solution 1 - DFS
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.number = n
        self.solution = [0] * n
        self.ans = []
        self.dfs(0)
        return self.ans

    def dfs(self, row):
        for col in range(self.number):
            ok = True
            for i in range(row):
                #same row is impossible
                #same col or diagnal
                if col == self.solution[i] or \
                    col - self.solution[i] == row - i or col - self.solution[i] == i - row:
                    ok = False
                    break
            if not ok:
                continue
            else:
                self.solution[row] = col
                if row == self.number - 1:
                    self.append_ans()
                else:
                    self.dfs(row + 1)

    def append_ans(self):
        solution = []
        for index, value in enumerate(self.solution):
            basic = ["."] * self.number
            basic[value] = "Q"
            solution.append(''.join(basic))
        self.ans.append(solution)

#Solution 1 - DFS pythonic
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.number = n
        self.solution = [0] * n
        self.ans = []
        self.dfs(0)
        return self.ans

    def dfs(self, row):
        for col in range(self.number):
            if any(col == self.solution[i] or 
                    col - self.solution[i] == row - i or 
                    col - self.solution[i] == i - row for i in range(row)):
                continue
            self.solution[row] = col
            if row == self.number - 1:
                self.append_ans()
            else:
                self.dfs(row + 1)

    def append_ans(self):
        solution = []
        for index, value in enumerate(self.solution):
            basic = ["."] * self.number
            basic[value] = "Q"
            solution.append(''.join(basic))
        self.ans.append(solution)

#Solution 2 - DFS with boolean array record
#三个boolean储存横竖撇是否占用
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.number = n
        self.ans = []
        self.solution = [0] * n
        # self.row_occupation = [False for _ in range(n)]
        self.col_occupation = [False for _ in range(n)]
        self.diagnal_left_occupation = [False for _ in range(2*n-1)]
        self.diagnal_right_occupation = [False for _ in range(2*n-1)]
        self.dfs(0)
        return self.ans

    def dfs(self, row):
        for col in range(self.number):
            number_left_diagnal = row + col
            number_right_diagnal = self.number - 1 - row + col
            if self.col_occupation[col] or \
                self.diagnal_left_occupation[number_left_diagnal] or \
                self.diagnal_right_occupation[number_right_diagnal]:
                continue
            self.solution[row] = col
            if row == self.number - 1:
                self.append_ans()
            else:
                self.col_occupation[col] = \
                    self.diagnal_left_occupation[number_left_diagnal] = \
                    self.diagnal_right_occupation[number_right_diagnal] = True
                self.dfs(row + 1)
                self.col_occupation[col] = \
                    self.diagnal_left_occupation[number_left_diagnal] = \
                    self.diagnal_right_occupation[number_right_diagnal] = False

    def append_ans(self):
        solution = []
        for index, value in enumerate(self.solution):
            basic = ["."] * self.number
            basic[value] = "Q"
            solution.append(''.join(basic))
        self.ans.append(solution)

#Solution 3 - DFS with bit array
#三个boolean储存横竖撇是否占用
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.number = n
        self.ans = []
        self.solution = [0] * n
        # self.row_occupation = [False for _ in range(n)]
        self.col_occupation = 0
        self.diagnal_left_occupation = 0
        self.diagnal_right_occupation = 0
        self.dfs(0)
        return self.ans

    def dfs(self, row):
        for col in range(self.number):
            number_left_diagnal = row + col
            number_right_diagnal = self.number - 1 - row + col
            if ((self.col_occupation >> col) | \
                (self.diagnal_left_occupation >> number_left_diagnal) | \
                (self.diagnal_right_occupation >> number_right_diagnal)) & 1:
                continue
            self.solution[row] = col
            if row == self.number - 1:
                self.append_ans()
            else:
                self.col_occupation ^= (1 << col)
                self.diagnal_left_occupation ^= (1 << number_left_diagnal)
                self.diagnal_right_occupation ^= (1 << number_right_diagnal)

                self.dfs(row + 1)

                self.col_occupation ^= (1 << col)
                self.diagnal_left_occupation ^= (1 << number_left_diagnal)
                self.diagnal_right_occupation ^= (1 << number_right_diagnal)

    def append_ans(self):
        solution = []
        for index, value in enumerate(self.solution):
            basic = ["."] * self.number
            basic[value] = "Q"
            solution.append(''.join(basic))
        self.ans.append(solution)

n = 5
#Expect
"""
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
r = Solution().solveNQueens(n)