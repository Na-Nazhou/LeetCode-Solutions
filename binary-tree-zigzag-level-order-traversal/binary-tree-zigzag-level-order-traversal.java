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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        
        q.offer(root);
        int level = 0;
        
        while (!q.isEmpty()) {
            int size = q.size();
            List<Integer> levelOrder = new ArrayList<>();
            
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                if (node == null) {
                    continue;
                }
                
                levelOrder.add(node.val);
                
                q.offer(node.left);
                q.offer(node.right);
            }
        
            if (level % 2 == 1) {
                Collections.reverse(levelOrder);
            }      
            
            if (!levelOrder.isEmpty()) {
                ans.add(levelOrder);
            }
            
            level++;
        }
        
        return ans;
    }
}
