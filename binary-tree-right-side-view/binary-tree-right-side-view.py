# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        if root is None:
            return ans
        
        q = deque()
        q.append(root)
        
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                
                if i == size - 1:
                    ans.append(node.val)
                    
                if node.left is not None:
                    q.append(node.left)
                
                if node.right is not None:
                    q.append(node.right)
        
        return ans