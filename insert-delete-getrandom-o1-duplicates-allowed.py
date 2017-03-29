class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.index = {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if not val in self.index:
            self.vals.append(val)
            self.index[val] = [len(self.vals) - 1]
            return True
        else:
            self.vals.append(val)
            self.index[val].append(len(self.vals) - 1)
            return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.index:
            val_index, last_val = self.index[val][-1], self.vals[-1]
            self.vals[val_index] = last_val
            last_val_index_in_map = self.index[last_val].index(len(self.vals) - 1)
            self.index[last_val][last_val_index_in_map] = val_index
            self.vals.pop()
            self.index[val].pop()
            if not self.index[val]:
                self.index.pop(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        import random
        if self.vals:
            return random.choice(self.vals)
        else:
            return None

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
t = ["RandomizedCollection","insert","remove","insert","remove","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom"]
[[],[0],[0],[-1],[0],[],[],[],[],[],[],[],[],[],[]]
t = ["RandomizedCollection","insert","insert","remove","insert","remove","getRandom"]
[[],[0],[1],[0],[2],[1],[]]
r = RandomizedCollection()
