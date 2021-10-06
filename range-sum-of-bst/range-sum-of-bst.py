# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        ans = 0
        
        def dfs(root):
            nonlocal ans
            
            if root is None:
                return
            
            val = root.val
            if val >= low and val <= high:
                ans += val
            
            if val < high:
                dfs(root.right)
            
            if val > low:
                dfs(root.left)
        
        dfs(root)
        
        return ans
            
                