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
    int ans = 0;
    boolean isFound = false;
    
    public int kthSmallest(TreeNode root, int k) {
        isFound = false;
        kthSmallestHelper(root, k);
        
        return ans;
    }
    
    private int kthSmallestHelper(TreeNode root, int k) {
        if (root == null) {
            return 0;
        }
        
        int leftSize = kthSmallestHelper(root.left, k);
        
        if (isFound) {
            return 0;
        }
        
        if (leftSize == k - 1) {
            ans = root.val;
            isFound = true;
            return 0;
        }
        
        
        int rightSize = kthSmallestHelper(root.right, k - leftSize - 1);
        
        return leftSize + rightSize + 1;
    }
}