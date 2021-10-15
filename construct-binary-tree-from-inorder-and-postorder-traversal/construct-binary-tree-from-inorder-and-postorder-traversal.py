# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # inorder: left, root, right
        # postorder: left, right, root

        val_to_idx = {}
        for i, val in enumerate(inorder):
            val_to_idx[val] = i

        post_idx = len(postorder) - 1
        
        def helper(i, j):
            if i > j:
                return None
            
            nonlocal post_idx
            val = postorder[post_idx]
            root = TreeNode(val)
            idx = val_to_idx[val]
            
            post_idx -= 1
            
            root.right = helper(idx + 1, j)
            root.left = helper(i, idx - 1)
            
            return root
        
        return helper(0, len(inorder) - 1)