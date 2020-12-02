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
class Solution {
    private int max = Integer.MIN_VALUE;
    
    public int maxPathSum(TreeNode root) {
        this.helper(root);
        return this.max;
    }
    
    private int helper(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = helper(root.left);
        int right = helper(root.right);
​
        int maxSimplePathSumRootedHere = Math.max(Math.max(left, right), 0) + root.val;
        int maxPathSumRootedHere = Math.max(maxSimplePathSumRootedHere, left + right + root.val);
        this.max = Math.max(this.max, maxPathSumRootedHere);
        return maxSimplePathSumRootedHere;
    }
}
