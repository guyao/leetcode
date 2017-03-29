"""
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        import collections
        return 1 == max(collections.Counter(
            x
            for i, row in enumerate(board)
            for j, c in enumerate(row)
            if c != '.'
            for x in ((c, i), (j, c), (i/3, j/3, c))
        ).values() + [1])


t = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
#expect True

t1 = [
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
t = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
#expect False
"""
..4...63.
.........
5......9.
...56....
4.3.....1
...7.....
...5.....
.........
.........
"""
r = Solution().isValidSudoku(t)

