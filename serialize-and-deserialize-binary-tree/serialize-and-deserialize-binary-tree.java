/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        
        StringBuilder sb = new StringBuilder();
        Stack<TreeNode> q = new Stack<>();
        q.push(root);
        
        while (!q.isEmpty()) {
            TreeNode node = q.pop();
            if (node == null) {
                sb.append("null");
            } else {
                sb.append(String.valueOf(node.val));
                q.push(node.right);
                q.push(node.left);
            }
            sb.append(",");   
        }
        
        sb.deleteCharAt(sb.length() - 1);
        return sb.toString();
    }
    
    private TreeNode deserializeHelper(Queue<String> vals) {
        String val = vals.poll();
        if (val.equals("null")) {
            return null;
        }
        
        TreeNode root = new TreeNode(Integer.parseInt(val));
        root.left = deserializeHelper(vals);
        root.right = deserializeHelper(vals);
        return root;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] values = data.split(",");
//         Queue<String> vals = new LinkedList();
//         for (String val : values) {
//             vals.offer(val);
//         }
//         TreeNode root = deserializeHelper(vals);
        
        Stack<TreeNode> stack = new Stack();
        TreeNode prev = null;
        TreeNode root = null;
        
        boolean setLeft = true;
        for (int ptr = 0; ptr < values.length; ptr++) {
            // System.out.println("See");
            // System.out.println(values[ptr]);
            
            String val = values[ptr];
            TreeNode node = val.equals("null") ? null : new TreeNode(Integer.parseInt(val));
            
            // Root node
            if (prev == null) {
                prev = node;
                root = node;
                stack.push(node);
                // System.out.println("Push");
                // System.out.println(node.val);
                continue;
            }
            
            if (node == null) {
                if (stack.isEmpty()) {
                    break;
                }
                prev = stack.pop();
                // System.out.println("Pop");
                // System.out.println(prev.val);
                setLeft = false;
                continue;
            }
            
            if (!setLeft) {
                prev.right = node;
                // System.out.printf("Set right child of %d to %d\n", prev.val, node.val);
                setLeft = true;
            } else {
                // System.out.printf("Set left child of %d to %d\n", prev.val, node.val);
                prev.left = node;
            }
            
            // System.out.println("Push");
            // System.out.println(node.val);
            
            stack.push(node);
            prev = node;
        }
        
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));