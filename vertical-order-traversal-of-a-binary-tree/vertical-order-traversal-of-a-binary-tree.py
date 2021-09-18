# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        m = defaultdict(dict)
        q = deque()
        if root is None:
            return []
        
        q.append((root, (0, 0)))
        while q:
            size = len(q)
            for _ in range(size):
                node, pos = q.popleft()
                if pos[0] not in m[pos[1]]:
                    m[pos[1]][pos[0]] = []
                m[pos[1]][pos[0]].append(node.val)
                if node.left is not None:
                    q.append((node.left, (pos[0] + 1, pos[1] - 1)))
                if node.right is not None:
                    q.append((node.right, (pos[0] + 1, pos[1] + 1)))
        
        ans = []
        cols = sorted(m.keys())
        for col in cols:
            order = []
            rows = sorted(m[col].keys())
            for row in rows:
                order += sorted(m[col][row])
            ans.append(order)
        
        return ans
                