class Solution {
    private List<List<Integer>> perms = new ArrayList<>();
    
    public List<List<Integer>> permuteUnique(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        permute(nums.length, map, new ArrayList<>());
        return perms;
    }
    
    private void permute(int n, Map<Integer, Integer> nums, List<Integer> curr) {
        if (curr.size() == n) {
            perms.add(new ArrayList<Integer>(curr));
            return;
        }
        
        for (int num : nums.keySet()) {
            if (nums.get(num) == 0) {
                continue;
            }
            
            nums.put(num, nums.get(num) - 1);
            curr.add(num);
            
            permute(n, nums, curr);
            
            nums.put(num, nums.get(num) + 1);
            curr.remove(curr.size() - 1);
        }    
    }
}
