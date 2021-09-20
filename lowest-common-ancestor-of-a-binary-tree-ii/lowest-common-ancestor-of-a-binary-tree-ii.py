# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = None
        
        def helper(root):
            nonlocal ans
            if root is None:
                return False
            
            left = helper(root.left)
            right = helper(root.right)
            
            curr = root == p or root == q
            
            if curr + left + right == 2:
                ans = root
                return True
            
            return left or right or curr
        
        helper(root)
        
        return ans