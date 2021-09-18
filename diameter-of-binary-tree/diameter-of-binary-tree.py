# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def helper(root):
            if root is None:
                return 0
            
            nonlocal ans
            
            left = helper(root.left)
            right = helper(root.right)
            
            ans = max(ans, left + right)
            
            return 1 + max(left, right)
        
        helper(root)
        
        return ans