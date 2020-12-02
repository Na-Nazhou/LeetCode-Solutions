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
    public List<List<Integer>> levelOrder(TreeNode root) {
        ArrayDeque<List<Integer>> order = levelOrderHelper(root);
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        Iterator<List<Integer>> it = order.iterator();
        while (it.hasNext()) {
            res.add(it.next());
        }
        return res;
    }
    
    private ArrayDeque<List<Integer>> levelOrderHelper(TreeNode root) {
        if (root == null) {
            return new ArrayDeque<>();
        }
        
        ArrayDeque<List<Integer>> left = levelOrderHelper(root.left);
        ArrayDeque<List<Integer>> right = levelOrderHelper(root.right);
        
        Iterator<List<Integer>> leftPtr = left.iterator();
        Iterator<List<Integer>> rightPtr = right.iterator();
        if (left.size() >= right.size()) {
            while (rightPtr.hasNext()) {
                leftPtr.next().addAll(rightPtr.next());
            }
        } else {
            while (leftPtr.hasNext()) {
                leftPtr.next().addAll(rightPtr.next());
            }
            while (rightPtr.hasNext()) {
                left.add(rightPtr.next());
            }
        }
        
        ArrayList<Integer> currLevel = new ArrayList<>(Arrays.asList(root.val));
        left.addFirst(currLevel);
        return left;
    }
}
