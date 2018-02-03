"""
https://leetcode.com/problems/h-index-ii

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = 0
        for c in reversed(citations):
            if c >= h + 1:
                h += 1
            else:
                break
        return h