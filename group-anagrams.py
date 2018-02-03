# https://leetcode.com/problems/group-anagrams
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        d = defaultdict(list)
        category = lambda word: tuple(sorted(list(word)))
        for word in strs:
            d[category(word)].append(word)
        return [d[k] for k in d]
