"""
Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
"""


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        n = len(beginWord)
        visited = set()
        wdl = set(wordList)
        nxt = []
        cur = [beginWord]
        dis = 0
        while cur:
            nxt = []
            for word in cur:
                if word == endWord:
                    return dis + 1
                for i in range(n):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        candidate = word[:i] + c + word[i + 1:]
                        if candidate not in visited and candidate in wdl:
                            nxt.append(candidate)
                            visited.add(candidate)
            cur = nxt
            dis += 1
        return 0
