# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) < 1:
            return None
        root_value = postorder[-1]
        root_index = inorder.index(root_value)
        r = TreeNode(root_value)
        r.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        r.right = self.buildTree(inorder[root_index + 1:], postorder[root_index:-1])
        return r


"""
   0
  1 2
3 4 5 6

preorder  : 0 1 3 4 2 5 6
inorder   : 3 1 4 0 5 2 6
postorder : 3 4 1 5 6 2 0
"""
inorder = [3, 1, 4, 0, 5, 2, 6]
postorder = [3, 4, 1, 5, 6, 2, 0]
r = Solution().buildTree(inorder, postorder)

        