/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
​
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> inorder = new ArrayList<>();
        
        pushLeft(stack, root);
        
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            inorder.add(node.val);
            pushLeft(stack, node.right);
        }
        
        return inorder;
    }
    
    private void pushLeft(Stack<TreeNode> stack, TreeNode root) {
        TreeNode curr = root;
        while (curr != null) {
            stack.push(curr);
            curr = curr.left;
        }
    }
}
