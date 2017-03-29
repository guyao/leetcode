class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}

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
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

obj = Trie()
obj.insert("apple")
obj.insert("apphone")