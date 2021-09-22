# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        
        q = deque()
        q.append(root)
        forward = True
        while q:
            size = len(q)
            next_q = deque()
            level = []
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            if forward:
                res.append(level)
            else:
                res.append(reversed(level))
            q = next_q
            forward = not forward
        
        return res