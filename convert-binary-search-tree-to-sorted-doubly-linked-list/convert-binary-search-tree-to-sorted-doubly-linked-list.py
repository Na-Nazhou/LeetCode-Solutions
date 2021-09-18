"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(root):
            if root.left is None and root.right is None:
                return (root, root)
            if root.left is None:
                right_start, right_end = dfs(root.right)
                root.right = right_start
                right_start.left = root
                return (root, right_end)
            if root.right is None:
                left_start, left_end = dfs(root.left)
                root.left = left_end
                left_end.right = root
                return (left_start, root)

            left_start, left_end = dfs(root.left)
            right_start, right_end = dfs(root.right)
            root.left = left_end
            left_end.right = root
            root.right = right_start
            right_start.left = root
            return left_start, right_end

        if root is None:
            return None

        start, end = dfs(root)
        start.left = end
        end.right = start
        
        # curr = start
        # while True:
        #     print(curr.val)
        #     curr = curr.right
        #     if curr == start:
        #         break

        return start