"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = zip(*matrix[::-1])

a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# a = [[1]]
# expect
"""
[7, 4, 1]
[8, 5, 2]
[9, 6, 3]
"""
r = Solution().rotate(a)

