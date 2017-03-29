"""
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.

Hint:
1. An easy approach is to sort the array first.
2. What are the possible values of h-index?
3. A faster approach is to use extra space.
"""
# 9%
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        citations.sort()
        citations.reverse()
        min_citation = 0
        h = 0
        for i, v in enumerate(citations):
            n = i + 1
            min_citation = v
            h = max(min(n, min_citation), h)
        return h
# 40%
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        length_list = [0 for _ in range(length + 1)]
        for i, v in enumerate(citations):
            if v > length:
                length_list[length] += 1
            else:
                length_list[v] += 1
        count = 0
        h_index = 0
        for i in reversed(range(len(length_list))):
            count += length_list[i]
            h_index = max(h_index, min(count, i))
        return h_index


t = [3, 0, 6, 1, 5]
r = Solution().hIndex(t)