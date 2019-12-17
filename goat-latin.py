class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = set("aeiouAEIOU")

        def process_word(w, i):
            # begin with vowel
            if w[0] in vowel:
                w = w + "ma"
            else:
                w = w[1:] + w[0] + "ma"
            return w + "a" * (i + 1)

        words = S.split()
        for i, w in enumerate(words):
            words[i] = process_word(w, i)
        return " ".join(words)