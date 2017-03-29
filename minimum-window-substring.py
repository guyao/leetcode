class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        INF = float('inf')
        count = len(t)
        m = {}
        for c in t:
            m[c] = 0
        for c in t:
            m[c] += 1
        begin = 0
        end = 0
        head = 0
        d = INF
        while end < len(s):
            if m.get(s[end]) is not None:
                if m[s[end]] > 0:
                    count -= 1
                m[s[end]] -= 1
            end += 1
            while count == 0:
                if end - begin < d:
                    d = end - begin
                    head = begin
                if m.get(s[begin]) is not None:
                    if m[s[begin]] == 0:
                        count += 1
                    m[s[begin]] += 1
                begin += 1
        return s[head:head+d] if d != INF else ""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        INF = float('inf')
        count = len(t)
        m = {}
        for c in t:
            m[c] = 0
        for c in t:
            m[c] += 1
        begin = 0
        end = 0
        head = 0
        d = INF
        while end < len(s):
            if m.get(s[end]) is not None:
                if m[s[end]] > 0:
                    count -= 1
                m[s[end]] -= 1
            end += 1
            print(head, begin, end, m, count)
            if count == 0:
                print("-"*20)
                while count == 0:
                    if end - begin < d:
                        d = end - begin
                        head = begin
                    if m.get(s[begin]) is not None:
                        if m[s[begin]] == 0:
                            count += 1
                        m[s[begin]] += 1
                    begin += 1
                    print(head, begin, end,m)
                print("-"*20)
        return s[head:head+d] if d != INF else ""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        INF = float('inf')
        import collections
        need, missing = collections.Counter(t), len(t)
        i = 0
        begin = 0
        end = INF
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            print(i, j, need)
            if not missing:
                print("+-----")
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if j - i <= end - begin:
                    begin, end = i, j
                print("-----+")
        return s[begin:end]



s = "ADOBECODEBANC"
t = "ABC"
#expect "BANC"
r = Solution().minWindow(s, t)
print(r)
