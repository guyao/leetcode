"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.

click to show hint.

You should be familiar with how a Trie works. If not, please work on this problem: Implement Trie (Prefix Tree) first.
"""

#Begin of Trie
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}

    def __repr__(self):
        return 'TreeNode({})'.format(self.leaves)

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        r = self.root
        for i, c in enumerate(word):
            if r.leaves.get(c) is None:
                r.leaves[c] = TrieNode()
            r = r.leaves[c]
            if i == len(word) - 1:
                r.is_string = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        r = self.root
        for c in word:
            if r.leaves.get(c) is None:
                return False
            r = r.leaves[c]
        return True if r.is_string else False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        r = self.root
        for c in prefix:
            if r.leaves.get(c) is None:
                return False
            r = r.leaves[c]
        return True
#End of Trie

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.trie.insert(word)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        root = self.trie.root
        return self.dfs(root, word, 0)

    def dfs(self, node, word, i):
        if i == len(word):
            return True and node.is_string
        word_to_search = word[i]
        result = False
        if word_to_search == ".":
            for c in node.leaves:
                result = result or self.dfs(node.leaves[c], word, i + 1)
        else:
            if node.leaves.get(word_to_search) is None:
                return False
            else:
                result = result or self.dfs(node.leaves[word_to_search], word, i + 1)
        return result


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
