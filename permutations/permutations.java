class Solution {
    private List<List<Integer>> perms = new ArrayList<>();
    
    public List<List<Integer>> permute(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        permute(nums.length, set, new ArrayList<>());
        return perms;
    }
    
    private void permute(int n, Set<Integer> nums, List<Integer> curr) {
        if (curr.size() == n) {
            perms.add(new ArrayList<Integer>(curr));
            return;
        }
        
        ArrayList<Integer> arr = new ArrayList<>(nums);
        for (int num : arr) {
            nums.remove(num);
            curr.add(num);
            permute(n, nums, curr);
            nums.add(num);
            curr.remove(curr.size() - 1);
        }    
    }
}
