# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def search(root, l, r):
            if root is None:
                return None
            if l <= root.val <= r:
                root.left = search(root.left, l, r)
                root.right = search(root.right, l, r)
                return root
            else:
                left = search(root.left, l, r)
                right = search(root.right, l, r)
                if left:
                    return left
                elif right:
                    return right
                else:
                    return None

        return search(root, L, R)