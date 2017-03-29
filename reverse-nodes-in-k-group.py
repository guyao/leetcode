"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        h = head
        prev = None
        fast_pointer = head
        slow_pointer = dummy
        count = 0
        while fast_pointer is not None:
            fast_pointer = fast_pointer.next
            count += 1
            if count == k:
                prev = slow_pointer
                ed = slow_pointer.next
                for i in range(count):
                    curr = h
                    h = h.next
                    curr.next = prev
                    prev = curr
                    count -= 1
                slow_pointer.next = prev
                ed.next = h
                slow_pointer = ed
        return dummy.next

def list_to_listnode(l):
    dummy = ListNode(0)
    p = dummy
    for i in l:
        p.next = ListNode(i)
        p = p.next
    return dummy.next

def traverse_linked_list(l):
    p = l
    while p is not None:
        import time
        time.sleep(0.5)
        print(p.val, end=" ")
        p = p.next

t = list_to_listnode([1,2,3,4,5])
r = Solution().reverseKGroup(t, 3)
traverse_linked_list(r)
