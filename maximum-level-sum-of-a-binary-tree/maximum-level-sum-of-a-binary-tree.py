# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        curr_max_sum = float("-inf")
        ans = None
        
        q = deque()
        q.append(root)
        level = 1
        
        while q:
            size = len(q)
            curr_sum = 0
            for _ in range(size):
                node = q.popleft()
                curr_sum += node.val
                for node in [node.left, node.right]:
                    if node is None:
                        continue        
                    q.append(node)
            
            if curr_sum > curr_max_sum:
                curr_max_sum = curr_sum
                ans = level
            
            level += 1
        
        return ans