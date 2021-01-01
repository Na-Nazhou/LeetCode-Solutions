class Solution {
    List<List<Integer>> answer = new ArrayList<>();
    
    public List<List<Integer>> subsets(int[] nums) {
        subsets(nums, 0, new ArrayList<>());
        return answer;
    }
    
    private void subsets(int[] nums, int i, List<Integer> curr) {
        if (i == nums.length) {
            answer.add(new ArrayList<>(curr));
            return;
        }
        
        for (; i < nums.length; i++) {
            curr.add(nums[i]);
            subsets(nums, i + 1, curr);
            curr.remove(curr.size() - 1);
        }
        
        subsets(nums, nums.length, curr);
    }
}
