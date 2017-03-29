"""

For example,
Given heights = [2,1,5,6,2,3],
return 10.
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        max_area = 0
        i = 0
        while i < len(heights):
            if len(stack) == 0 or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                    curr_i = stack.pop()
                    area = heights[curr_i]*( i - (stack[-1] + 1)if len(stack) > 0 else i)
                    max_area = max(max_area, area)
        while len(stack) > 0:
            curr_i = stack.pop()
            while len(stack) > 0 and heights[curr_i] == heights[stack[-1]]:
                stack.pop()
            area = heights[curr_i]*( i - (stack[-1] + 1) if len(stack) > 0 else i)
            max_area = max(max_area, area)
        return max_area

t = [2,1,5,6,2,3]
t = [1]
t = [1, 2, 3]
t = [3, 2, 1]
t = [2,1,5,6,2,3]
t = [1, 1]
t = [2, 3]
t = [5,4,4,6,3,2,9,5,4,8,1,0,0,4,7,2]

r = Solution().largestRectangleArea(t)