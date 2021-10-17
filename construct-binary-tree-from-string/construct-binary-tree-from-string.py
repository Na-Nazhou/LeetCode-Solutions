# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        
        i = 0
        def dfs():
            nonlocal i
            
            if i >= len(s):
                return None
            
            # if s[i] == ')':
            #     i += 1
            #     return None
            

            is_negative = False
            if s[i] == '-':
                is_negative = True
                i += 1
            
            curr = 0
            while i < len(s) and s[i].isdigit():
                curr = curr * 10 + int(s[i])
                i += 1
            if is_negative:
                curr = -curr
            
            # i = 1
            # curr = 4
            
            root = TreeNode(curr)
            
            # root = TreeNode(4)
            
            if i < len(s) and s[i] == '(':
                i += 1
                root.left = dfs()
            
                        
            if i < len(s) and s[i] == '(':
                i += 1
                root.right = dfs()
            
            i += 1
            return root
        
        return dfs()
            