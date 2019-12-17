from collections import defaultdict

class ValidWordAbbr:

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        hashed = defaultdict(set)

        for w in dictionary:
            digest = self.hash_word(w)
            hashed[digest].add(w)

        self.hashed = hashed

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        digest = self.hash_word(word)
        words = self.hashed[digest]
        if not words:
            return True
        else:
            if len(words) == 1 and word in words: return True
            else: return False
    
    def hash_word(self, w):
        if len(w) <= 2: return w
        return w[0] + str(len(w) - 2) + w[-1]