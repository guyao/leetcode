# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

# Hash table O(n) runtime, O(n) space
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dummy = RandomListNode(0)
        p = dummy
        h = head
        m = {}
        while h is not None:
            node = RandomListNode(h.label)
            p.next = node
            m[h] = node
            h = h.next
            p = p.next
        p = dummy.next
        h = head
        while h is not None:
            p.random = m[h.random] if h.random is not None else None
            p = p.next
            h = h.next
        return dummy.next

# modify original structure
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        h = head
        while h is not None:
            node = RandomListNode(h.label)
            h.next, node.next = node, h.next
            h = h.next.next
        h = head
        while h is not None:
            h.next.random = h.random.next if h.random is not None else None
            h = h.next.next
        h = head
        copyhead = h.next if h is not None else None
        while h is not None:
            copy = h.next
            h.next = copy.next
            h = h.next
            copy.next = h.next if h is not None else None
        return copyhead


n1 = RandomListNode(1)
n2 = RandomListNode(2)
n3 = RandomListNode(3)
n1.next = n2
n2.next = n3
n1.random = n2
n2.random = n1
n3.random = n3
n1 = RandomListNode(-1)
n1.next = None
r = Solution().copyRandomList(n1)

"""
Note:
* input {}
* in the original structure solution: change back the original pointer
"""
