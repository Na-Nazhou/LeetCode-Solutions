# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if root is None:
            return 
        
        def dfs(root):
            if root is None:
                return None
           
            left_right_tail = dfs(root.left)
            right_right_tail = dfs(root.right)
            
            if left_right_tail is not None:
                left_right_tail.right = root.right
            if root.left is not None:
                root.right = root.left
            root.left = None
            
            if right_right_tail is not None:
                return right_right_tail
            
            if left_right_tail is not None:
                return left_right_tail
            
            return root
        
        dfs(root)
        
        return root