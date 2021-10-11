# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root)
        res = []
        while q:
            count = len(q)
            curr_sum = 0
            for _ in range(count):
                node = q.popleft()
                curr_sum += node.val
                for child in [node.left, node.right]:
                    if child is not None:
                        q.append(child)
            avg = curr_sum / count
            res.append(avg)
        return res