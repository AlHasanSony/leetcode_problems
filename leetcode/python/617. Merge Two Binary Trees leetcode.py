#problem link -  https://leetcode.com/problems/merge-two-binary-trees/

class Solution(object):
    def mergeTrees(self, r1, r2):
        """
        :type r1: TreeNode
        :type r2: TreeNode
        :rtype: TreeNode
        """
        if r1 == None and r2 == None:
            return None
        elif r1 == None:
            return r2
        elif r2 == None:
            return r1
        else:
            root = TreeNode(r1.val + r2.val)
            root.left = self.mergeTrees(r1.left, r2.left)
            root.right = self.mergeTrees(r1.right, r2.right)
            return root