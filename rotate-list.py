# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return 'LinkedList({})'.format(self.val)

def deserialize(l):
    dummy = ListNode(None)
    head = dummy
    for i in l:
        head.next = ListNode(i)
        head = head.next
    return dummy.next

def pl(head):
    while head is not None:
        print(head)
        head = head.next


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head is None:
            return None
        if k == 0:
            return head

        dummy = ListNode(None)
        dummy.next = head

        fast = dummy
        slow = dummy

        for _ in range(k):
            if fast.next is not None:
                fast = fast.next
            else:
                fast = dummy.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        if slow is not dummy:
            dummy.next, fast.next, slow.next = slow.next, head, None
        return dummy.next

"""
Test Cases
l = [1,2,3]
k = 20000

better performance if count the length before
"""

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        dummy = ListNode(None)
        dummy.next = head

        p = head
        l = 0
        while p is not None:
            p = p.next
            l += 1
        if l == 0:
            return None
        if k % l:
            step = l - k % l
            tail = dummy
            for _ in range(step):
                tail = tail.next
            new_head = tail.next
            tail.next = None

            mid = new_head
            while mid.next is not None:
                mid = mid.next
            mid.next = head
            dummy.next = new_head
        return dummy.next

l = [1,2,3]
k = 20000

l = []
k = 0
head = deserialize(l)
r = Solution().rotateRight(head, k)