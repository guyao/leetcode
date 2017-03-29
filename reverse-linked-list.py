# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# iteratively
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head is not None:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        return self.reverseHelper(prev, head)


    def reverseHelper(self, prev, head):
        if head is None:
            return prev
        ret = self.reverseHelper(head, head.next)
        head.next = prev
        return ret

def list_to_listnode(l):
    dummy = ListNode(0)
    p = dummy
    for i in l:
        p.next = ListNode(i)
        p = p.next
    return dummy.next

t = list_to_listnode([1,2,3,4,5,6,7,8,9,10])
r = Solution().reverseList(t)
