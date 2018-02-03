class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def traverse(root):
            if root is None:
                return []
            return traverse(root.left) + [root.val] + traverse(root.right)
        return traverse(root)