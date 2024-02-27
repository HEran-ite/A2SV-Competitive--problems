# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root,lroot,rroot):
            if not root :
                return True
            if not (lroot < root.val < rroot):
                return False
        
            return (helper (root.left,lroot,root.val) and helper(root.right,root.val,rroot))
        return helper(root,float(-inf),float(inf))
         

