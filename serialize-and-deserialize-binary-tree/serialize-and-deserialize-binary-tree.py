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
        def dfs(root):
            if root is None:
                res.append("None")
                return
            
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        data = data.split(",")
        
        ptr = 0
        def dfs():
            nonlocal ptr
            val = data[ptr]
            ptr += 1
            
            if val == "None":
                return None
            
            root = TreeNode(int(val))
            root.left = dfs()
            root.right = dfs()
            
            return root
    
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))