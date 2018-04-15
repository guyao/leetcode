class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def merge(r1, r2):
            if not r1 and not r2:
                return None
            r = TreeNode((r1.val if r1 else 0) + (r2.val if r2 else 0))
            r.left = merge(r1.left if r1 else None, r2.left if r2 else None)
            r.right = merge(r1.right if r1 else None, r2.right if r2 else None)
            return r

        return merge(t1, t2)