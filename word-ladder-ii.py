"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]

"""
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_list = set(wordList)
        word_list.add(beginWord)
        result = []
        cur = [beginWord]
        visited = set([beginWord])
        found = False
        trace = {word: [] for word in word_list}
        while cur and not found:
            for word in cur:
                visited.add(word)
            nxt = set()
            for word in cur:
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i+1:]
                        if candidate not in visited and candidate in word_list:
                            if candidate == endWord:
                                found = True
                            nxt.add(candidate)
                            trace[candidate].append(word)
            cur = nxt
        if found:
            self.backtrace(result, trace, [], endWord)
        return result

    def backtrace(self, result, trace, path, word):
        if not trace[word]:
            result.append([word] + path)
        else:
            for prev in trace[word]:
                self.backtrace(result, trace, [word] + path, prev)

bg = "hit"
ed = "cog"
wdlst = ["hot","dot","dog","lot","log","cog"]
r = Solution().findLadders(bg, ed, wdlst)
