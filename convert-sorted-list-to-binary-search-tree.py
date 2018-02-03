class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def helper(head, tail):
            fast = head
            slow = head
            if head == tail:
                return None
            while (fast.next != tail) and (fast.next.next != tail):
                slow = slow.next
                fast = fast.next.next
            root = TreeNode(slow.val)
            root.left = helper(head, slow)
            root.right = helper(slow.next, tail)
            return root
        return helper(head, None)


class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        def get_length(head):
            size = 0
            while head is not None:
                size += 1
                head = head.next
            return size
        self.size = get_length(head)
        self.cur = head

        def helper(size):
            if size <= 0:
                return None
            left = helper(size // 2)
            root = TreeNode(self.cur.val)
            self.cur = self.cur.next
            right = helper(size - size // 2 - 1)
            root.left = left
            root.right = right
            return root

        return helper(self.size)