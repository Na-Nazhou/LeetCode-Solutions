# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        by_cols = defaultdict(list)
        
        q = deque()
        q.append((root, 0))
        
        min_col = 0
        max_col = 0
        
        while q:
            node, col = q.popleft()
            by_cols[col].append(node.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            
            if node.left is not None:
                q.append((node.left, col - 1))
            if node.right is not None:
                q.append((node.right, col + 1))
        
        res = []
        for col in range(min_col, max_col + 1):
            if col in by_cols:
                res.append(by_cols[col])
        
        return res