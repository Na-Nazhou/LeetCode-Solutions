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
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root, null, null);
    }
    
    private boolean isValidBST(TreeNode root, Integer max, Integer min) {
        if (root == null) {
            return true;
        }
        
        TreeNode left = root.left;
        TreeNode right = root.right;
        
        int rootVal = root.val;
        
        if (max != null && rootVal >= max) {
            return false;
        }
        
        if (min != null && rootVal <= min) {
            return false;
        }
        
        boolean isLeftValid;
        if (max == null) {
            isLeftValid = isValidBST(left, rootVal, min);
        } else {
            isLeftValid = isValidBST(left, Math.min(max, rootVal), min);
        }
        
        boolean isRightValid;
        if (min == null) {
            isRightValid = isValidBST(right, max, rootVal);
        } else {
            isRightValid = isValidBST(right, max, Math.max(min, rootVal));
        }
        
        return isLeftValid && isRightValid;
    }
}