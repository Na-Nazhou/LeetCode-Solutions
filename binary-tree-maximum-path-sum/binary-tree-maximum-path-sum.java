/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int ans = Integer.MIN_VALUE;
    
    public int maxPathSum(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        maxPathToLeafSum(root);
        
        return ans;
    }
    
    // Return height
    private int maxPathToLeafSum(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        int leftMaxSum = Math.max(maxPathToLeafSum(root.left), 0);
        int rightMaxSum = Math.max(maxPathToLeafSum(root.right), 0);
        
        // Update ans
        ans = Math.max(ans, leftMaxSum + rightMaxSum + root.val);
        
        return Math.max(leftMaxSum, rightMaxSum) + root.val;
    }
}