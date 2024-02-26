# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # try to use helper function that take in both the left and the right node of ur root
        # it will be easy since the isSymmetric function only take the root
        
        def helper(ltree,rtree):
            if not ltree and not rtree:
                return True
            if not rtree or not ltree:
                return False
            if rtree.val!=ltree.val:
                return False
        
            return helper(ltree.left,rtree.right) and helper (ltree.right,rtree.left)
        return helper(root.left,root.right)