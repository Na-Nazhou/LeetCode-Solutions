# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = None
        
        def dfs(root):
            nonlocal ans
            
            if root is None:
                return 0
            
            count = 0
            if root == p or root == q:
                count += 1
            count += dfs(root.left)
            count += dfs(root.right)
            
            if count == 2 and ans is None:
                ans = root
            
            return count
        
        dfs(root)
        
        return ans