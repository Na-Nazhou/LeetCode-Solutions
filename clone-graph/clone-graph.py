"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':        
        nodes = {}
        
        def dfs(root):
            if root is None:
                return None
            
            if root in nodes:
                return nodes[root]
            
            root_copy = Node(root.val)
            nodes[root] = root_copy
            for neighbor in root.neighbors:
                root_copy.neighbors.append(dfs(neighbor))
            
            return root_copy
        
        return dfs(node)