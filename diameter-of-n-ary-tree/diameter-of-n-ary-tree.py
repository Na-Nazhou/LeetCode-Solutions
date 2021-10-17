"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        
        ans = 0
        
        def dfs(root):
            nonlocal ans
            
            if root is None:
                return 0
            
            largest = 0
            second_largest = 0
            for child in root.children:
                height = dfs(child)
                
                if height >= largest:
                    second_largest = largest
                    largest = height
                    continue
                
                if height >= second_largest:
                    second_largest = height
            
            ans = max(ans, largest + second_largest)
            
            return largest + 1
        
        dfs(root)
        
        return ans
                    
                