"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        nodes = {} # original -> copy
        
        def dfs(root):
            if root is None:
                return None
            if root in nodes:
                return nodes[root]
            
            root_copy = Node(root.val)
            nodes[root] = root_copy
            
            root_copy.next = dfs(root.next)
            root_copy.random = dfs(root.random)
            
            return root_copy
        
        return dfs(head)