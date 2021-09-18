# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -float("inf")
        def helper(root):
            if root is None:
                return 0
            
            nonlocal ans
            
            left = max(helper(root.left), 0)
            right = max(helper(root.right), 0)
            
            ans = max(ans, root.val + left + right)
            
            return root.val + max(left, right)
        
        helper(root)
        
        return ans