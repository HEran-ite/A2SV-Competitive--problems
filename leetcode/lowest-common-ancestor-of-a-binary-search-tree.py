# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        p_path = []
        q_path = []


        def search(root, val, path):

            path.append(root)
            if root.val == val:
                return
            
            if root.val < val:
                search(root.right, val, path)
            
            else:
                search(root.left, val, path)

        
        search(root, p.val, p_path)
        search(root, q.val, q_path)


        for i in range(min(len(q_path), len(p_path))):

            if p_path[i] != q_path[i]:
                return p_path[i-1]
        
        return p_path[-1] if len(p_path) < len(q_path) else q_path[-1]
            




        

        
