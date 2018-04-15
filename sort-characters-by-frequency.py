class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        counter = Counter(s)
        return " ".join([c * freq for freq, c in reversed(sorted([(counter[k], k) for k in counter]))])