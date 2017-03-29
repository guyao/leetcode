class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.index = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if not val in self.index:
            self.vals.append(val)
            self.index[val] = len(self.vals) - 1
            return True
        else:
            return False





    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.index:
            val_index = self.index[val]
            last_value = self.vals[-1]
            self.vals[val_index] = last_value
            self.index[last_value] = val_index
            self.vals.pop()
            self.index.pop(val)
            return True            
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        if self.vals:
            return random.choice(self.vals)
        else:
            return None

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
r = RandomizedSet()