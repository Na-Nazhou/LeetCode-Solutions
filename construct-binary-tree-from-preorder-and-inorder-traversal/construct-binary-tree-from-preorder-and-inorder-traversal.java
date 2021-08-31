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
    int preorderIdx = 0;
    Map<Integer, Integer> idxMap = new HashMap<>();
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for (int i = 0; i < inorder.length; i++) {
            idxMap.put(inorder[i], i);
        }
        
        return buildTree(preorder, 0, preorder.length - 1);
    }
    
    private TreeNode buildTree(int[] preorder, int left, int right) {
        if (left > right) {
            return null;
        }   
        
        int rootVal = preorder[preorderIdx];
        preorderIdx++;
        TreeNode root = new TreeNode(rootVal);
        root.left = buildTree(preorder, left, idxMap.get(rootVal) - 1);
        root.right = buildTree(preorder, idxMap.get(rootVal) + 1, right);
        return root;
    }
}