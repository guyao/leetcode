"""
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.q = []
        def _iter(lst):
            for i in lst:
                if type(i) == list:
                    for j in _iter(i):
                        yield j
                else:
                    yield i
        self.iter = _iter(nestedList)

    def next(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            if not self.hasNext():
                raise StopIteration
        return self.q.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.q) != 0:
            return True
        else:
            try:
                v = next(self.iter)
                self.q.append(v)
                return True
            except StopIteration:
                return False
#Leetcode Submission
"""
class NestedIterator(object):

    def __init__(self, nestedList):
        self.q = []
        def _iter(lst):
            for i in lst:
                if i.isInteger():
                    yield i.getInteger()
                else:
                    for j in _iter(i.getList()):
                        yield j
        self.iter = _iter(nestedList)

    def next(self):
        if len(self.q) == 0:
            if not self.hasNext():
                raise StopIteration
        return self.q.pop(0)

    def hasNext(self):
        if len(self.q) != 0:
            return True
        else:
            try:
                v = next(self.iter)
                self.q.append(v)
                return True
            except StopIteration:
                return False
"""


#Stack of [list, index] pairs
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList, 0]]

    def next(self):
        if self.hasNext():
            l, i = self.stack[-1]
            self.stack[-1][1] += 1
            return l[i]

    def hasNext(self):
        s = self.stack
        while s:
            l, i = s[-1]
            if len(l) == i:
                s.pop()
            else:
                v = l[i]
                if type(v) is int:
                    return True
                else:
                    s[-1][1] += 1
                    s.append([v, 0])
        return False

#Leetcode submission
"""
class NestedIterator(object):
    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]

    def next(self):
        if self.hasNext():
            l, i = self.stack[-1]
            self.stack[-1][1] += 1
            return l[i].getInteger()

    def hasNext(self):
        s = self.stack
        while s:
            l, i = s[-1]
            if len(l) == i:
                s.pop()
            else:
                v = l[i]
                if v.isInteger():
                    return True
                else:
                    s[-1][1] += 1
                    s.append([v.getList(), 0])
        return False
"""