# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        lst=[]
        res=[]
        def inorder (root):
            if not root:
                return []
            inorder(root.left)
            lst.append(root.val)
            inorder(root.right)
        inorder(root)

        dic=Counter(lst)
        mx=max(dic.values())
        for num in dic:
            if dic[num]==mx:
                res.append(num)
        return res