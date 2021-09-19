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
                return (False, False)
            
            left = helper(root.left)
            right = helper(root.right)
            p_in_subtree = left[0] or right[0]
            q_in_subtree = left[1] or right[1]
            
            
            if root == p:
                if q_in_subtree:
                    ans = root
                    return (True, True)
                else:
                    return (True, False)
            
            if root == q:
                if p_in_subtree:
                    ans = root
                    return (True, True)
                else:
                    return (False, True)
            
            if (left[0] and right[1]) or (left[1] and right[0]):
                ans = root
                return (True, True)
            
            return (p_in_subtree, q_in_subtree)
        
        helper(root)
        
        return ans
                