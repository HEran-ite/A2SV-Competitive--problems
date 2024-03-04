# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        queue=deque([[root,1,0]])
        pl,pn=0,1

        while queue:
            root,n,l= queue.popleft()

            if l >pl:
                pl=l
                pn=n

            res=max(res,n-pn+1)
            if root.left:
                queue.append([root.left,2*n,l+1])
            if root.right:
                queue.append([root.right,2*n+1,l+1])
        return res