# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        queue=deque([])
        if root:
            queue=deque([root])
        flag=False
        while queue:
            level=[]
            for i in range (len(queue)):
                level.append(queue[0].val)
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                queue.popleft()
            if flag:
                level.reverse()   
                flag=False
            else:
                flag=True
            res.append(level)
        return res