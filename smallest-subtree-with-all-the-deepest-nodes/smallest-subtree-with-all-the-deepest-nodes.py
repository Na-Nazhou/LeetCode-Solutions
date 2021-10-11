# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def dfs(root):
            if root is None:
                return None, 0
            
            ans_left, left_height = dfs(root.left)
            ans_right, right_height = dfs(root.right)
            
            if left_height > right_height:
                return ans_left, left_height + 1
            if right_height > left_height:
                return ans_right, right_height + 1
                
            return root, left_height + 1
        
        return dfs(root)[0]