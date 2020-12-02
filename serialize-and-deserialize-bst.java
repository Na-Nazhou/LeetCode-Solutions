/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {
​
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        postOrder(root, sb);
        if (sb.length() > 0) {
            sb.deleteCharAt(sb.length() - 1);
        }
        
        return sb.toString();
    }
    
    private void postOrder(TreeNode root, StringBuilder sb) {
        if (root == null) {
            return;
        }
        
        postOrder(root.left, sb);
        postOrder(root.right, sb);
        sb.append(root.val);
        sb.append(" ");
    }
​
    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.isEmpty()) {
            return null;
        }
        
        ArrayDeque<Integer> values = new ArrayDeque<>();
        for (String valStr : data.split(" ")) {
            values.addLast(Integer.parseInt(valStr));
        }
        
        return buildTree(values, Integer.MIN_VALUE, Integer.MAX_VALUE);
        
    }
    
    private TreeNode buildTree(ArrayDeque<Integer> values, int min, int max) {
        if (values.isEmpty()) {
            return null;
        }
        
        int val = values.getLast();
        // Check whether the next number belongs to this subtree
        if (val < min || val >= max) {
            return null;
        }
        
        values.removeLast();
​
        TreeNode root = new TreeNode(val);
        root.right = buildTree(values, val, max);
        root.left = buildTree(values, min, val);
        
        return root;
    }
}
​
// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// String tree = ser.serialize(root);
// TreeNode ans = deser.deserialize(tree);
// return ans;
