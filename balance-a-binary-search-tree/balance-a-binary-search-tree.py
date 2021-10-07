# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        
        def inorder(root):
            if root is None:
                return
            
            inorder(root.left)
            arr.append(root)
            inorder(root.right)
        
        def buildTree(i, j):
            if i > j:
                return None
            
            mid = (i + j) // 2
            
            root = arr[mid]
            root.left = buildTree(i, mid - 1)
            root.right = buildTree(mid + 1, j)
            
            return root
        
        inorder(root)
        return buildTree(0, len(arr) - 1)