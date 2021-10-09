# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def dfs(root, parent):
            if root is None:
                return
            
            root.parent = parent
            dfs(root.left, root)
            dfs(root.right, root)
            
        dfs(root, None)
        
        q = Deque([target])
        visited = set([target])
        dist = 0
        while q:
            if dist == k:
                return [node.val for node in q]
            
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                for neighbor in [node.left, node.right, node.parent]:
                    if neighbor is not None and neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
            
            dist += 1
        
        return []
                        
            
            