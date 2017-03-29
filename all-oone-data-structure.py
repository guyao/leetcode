class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.data = [[]]

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.map:
            x, y = self.map[key]
            # val = self.data[x][y]
            self.data[x].pop(self.data[x].index(key))
            if len(self.data) < x + 1 + 1:
                self.data.append([])
            self.data[x+1].append(key)
            self.map[key] = (x+1, len(self.data[x+1]) - 1)
        else:
            self.data[1-1].append(key)
            self.map[key] = (0, len(self.data[0]) - 1)



    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.map:
            x, y = self.map[key]
            self.data[x].pop(self.data[x].index(key))
            if x-1 < 0:
                self.map.pop(key)
            else:
                self.data[x-1].append(key)
                self.map[key] = (x-1, len(self.data[x-1]) - 1)
        else:
            pass
        

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        import random
        for l in reversed(self.data):
            if l:
                return random.choice(l)
                break
        return ""
        # index = len(self.data) - 1
        # while index >= 0 and not self.data[index]:
            # index -= 1
        # return random.choice(self.data[index]) if 0 < index else ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        import random
        for l in self.data:
            if l:
                return random.choice(l)
                break
        return ""
        # index = 0
        # while index <= len(self.data) - 1 and not self.data[index]:
            # index += 1
        # return random.choice(self.data[index]) if index < len(self.data) else ""

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
t = ["AllOne","inc","inc","inc","inc","getMaxKey","inc","inc","inc","dec","inc","inc","inc","getMaxKey"]
[[],["hello"],["goodbye"],["hello"],["hello"],[],["leet"],["code"],["leet"],["hello"],["leet"],["code"],["code"],[]]

t = ["AllOne","inc","getMaxKey","getMinKey"]
[[],["hello"],[],[]]

t = ["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"]
[[],["hello"],["hello"],[],[],["leet"],[],[]]

t = ["AllOne","inc","inc","inc","inc","inc","dec","getMaxKey","getMinKey","inc","inc","inc","getMaxKey","getMinKey","inc","inc","getMinKey"]
[[],["hello"],["hello"],["world"],["world"],["hello"],["world"],[],[],["world"],["world"],["leet"],[],[],["leet"],["leet"],[]]

r = AllOne()