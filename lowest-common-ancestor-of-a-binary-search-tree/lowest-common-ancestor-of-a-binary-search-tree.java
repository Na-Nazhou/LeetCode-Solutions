/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) {
            return root;
        }
        
        if (q.val > p.val) {
            TreeNode temp = p;
            p = q;
            q = temp;
        }
        
        int rootVal = root.val;
        if (rootVal == p.val || rootVal == q.val) {
            return root;
        }
        
        boolean pPos = p.val < root.val; // true -> left subtree
        boolean qPos = q.val < root.val;
        
        if (pPos != qPos) {
            return root;
        } else if (pPos) {
            return lowestCommonAncestor(root.left, p, q);
        } else {
            return lowestCommonAncestor(root.right, p, q);
        }
    }
}