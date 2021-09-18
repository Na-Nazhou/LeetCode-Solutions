# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    def inorder(self, root, res):
        if root is None:
            return
        
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

    def __init__(self, root: Optional[TreeNode]):
        self.res = []
        self.inorder(root, self.res)
        self.ptr = 0

    def next(self) -> int:
        val = self.res[self.ptr]
        self.ptr += 1
        return val

    def hasNext(self) -> bool:
        return self.ptr < len(self.res)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()