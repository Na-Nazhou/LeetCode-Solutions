"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        path = set()
        
        curr = p
        while curr is not None:
            path.add(curr)
            curr = curr.parent
        
        curr = q
        while curr is not None:
            if curr in path:
                return curr
            curr = curr.parent
        
        raise ValueError('Unexpected')