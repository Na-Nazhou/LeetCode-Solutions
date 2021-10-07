# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(root):
            nonlocal ans
            
            if root is None:
                return 0
            
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            ans = max(ans, left_height + right_height)
            
            return max(left_height, right_height) + 1
        
        dfs(root)
        
        return ans