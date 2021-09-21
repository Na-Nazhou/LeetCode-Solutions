# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        
        m = defaultdict(list)
        pq = deque()
        pq.append((root, (0, 0)))
        min_col = 0
        max_col = 0
        
        while pq:
            node, pos = pq.popleft()
            m[pos[1]].append((pos[0], len(m[pos[1]]), node.val))
            min_col = min(min_col, pos[1])
            max_col = max(max_col, pos[1])
            
            if node.left is not None:
                pq.append((node.left, (pos[0] + 1, pos[1] - 1)))
            if node.right is not None:
                pq.append((node.right, (pos[0] + 1, pos[1] + 1)))
        
        for col in range(min_col, max_col + 1):
            if col in m:
                res.append([ val for _, _, val in sorted(m[col])])
        
        return res