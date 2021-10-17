# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        ans = root.val
        def dfs(root):
            nonlocal ans
            
            if root is None:
                return
            
            if abs(root.val - target) < abs(ans - target):
                ans = root.val
            
            if root.val == target:
                return
            elif root.val < target:
                dfs(root.right)
            else:
                dfs(root.left)
        
        dfs(root)
        
        return ans