# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def helper(root):
            if root is None:
                res.append("None")
                return
            
            res.append(str(root.val))
            helper(root.left)
            helper(root.right)
        
        helper(root)
        
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        res = data.split(",")
        q = deque(res)
        
        def helper():
            val = q.popleft()
            if val == "None":
                return None
            
            root = TreeNode(int(val))
            root.left = helper()
            root.right = helper()
            
            return root
        
        return helper()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))