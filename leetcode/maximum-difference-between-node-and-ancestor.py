# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        dif=[]
        def helper(root,mx,mn,dif):
            
            if not root:
                max_dif=mx-mn
                dif.append(max_dif)
                return 

            root.right=helper(root.right,max(root.val,mx),min(root.val,mn),dif)
            root.left=helper(root.left,max(root.val,mx),min(root.val,mn),dif)

        helper(root,float(-inf),float(inf),dif)
        return max(dif) 
        