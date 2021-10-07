# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, curr):
            curr = curr * 10 + root.val
            if root.left is None and root.right is None:
                return curr
            
            ans = 0
            if root.left is not None:
                ans += dfs(root.left, curr)
            if root.right is not None:
                ans += dfs(root.right, curr)
            
            return ans
        
        if root is None:
            return 0
        
        return dfs(root, 0)