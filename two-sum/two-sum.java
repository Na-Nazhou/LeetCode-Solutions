class Solution {
    // Time complexity: O(n)
    // Space complexity: O(n)
    public int[] twoSum(int[] nums, int target) {
        // key: number; value: index
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (map.containsKey(target - num)) {
                return new int[]{map.get(target - num), i};
            } else {
                map.put(num, i);
            }
        }
        
        throw new IllegalArgumentException("Solution not found.");
    }
}