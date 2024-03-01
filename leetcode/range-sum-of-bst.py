# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def summ(root):
            if not root:
                return 0

            root.left=summ(root.left)
            root.right=summ(root.right)

            if root.val<=high and root.val>=low:
                return root.left+root.right+root.val

            return root.left+root.right
            
        return summ(root)