# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nums):
            if not nums:
                return
            mx = float(-inf)
            idx = 0
            for i in range(len(nums)):
                if nums[i] > mx:
                    mx = nums[i]
                    idx = i
            
            root = TreeNode(mx)
            root.left = helper(nums[0:idx])
            root.right = helper(nums[idx+1:])
            return root
        return helper(nums)