# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        ans = None
        def helper(root):
            nonlocal ans
            
            if root is None:
                return
            
            if root.val == target:
                ans = root.val
                return
            
            if target > root.val:
                helper(root.right)
            else:
                helper(root.left)
            
            if ans is None or abs(root.val - target) < abs(ans - target):
                ans = root.val
        
        helper(root)
        
        return ans