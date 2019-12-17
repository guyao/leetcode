class StockSpanner:

    def __init__(self):
        self.s = []
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        res = 1
        while (self.s) and (self.s[-1][0] <= price):
            res += self.s.pop()[1]
        self.s.append((price, res))
        return res