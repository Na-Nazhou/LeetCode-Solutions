# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        min_col = 0
        max_col = 0
        
        ans = []
        if root is None:
            return ans
        
        q = deque()
        q.append((root, (0, 0)))
        
        nodes_by_col = defaultdict(list)
        
        while q:
            node, [row, col] = q.popleft()
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            
            nodes_by_col[col].append((row, node.val))
            
            if node.left:
                q.append((node.left, (row + 1, col - 1)))
            if node.right:
                q.append((node.right, (row + 1, col + 1)))
        
        for col in range(min_col, max_col + 1):
            if col in nodes_by_col:
                ans.append([ val for _, val in sorted(nodes_by_col[col])])
        
        return ans