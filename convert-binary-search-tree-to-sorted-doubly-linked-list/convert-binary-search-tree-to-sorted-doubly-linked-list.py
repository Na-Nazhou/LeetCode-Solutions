"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        
        def helper(root):
            ans_left = root
            ans_right = root
            
            if root.left is not None:
                left, right = helper(root.left)
                
                root.left = right
                right.right = root
                
                ans_left = left
            
            if root.right is not None:
                left, right = helper(root.right)
                
                root.right = left
                left.left = root
                
                ans_right = right
            
            return ans_left, ans_right
        
        if root is None:
            return None
        
        left, right = helper(root)
        
        left.left = right
        right.right = left
        
        return left