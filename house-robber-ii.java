class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        if (nums.length == 1) {
            return nums[0];
        }
        return Math.max(rob(nums, 0, nums.length - 1), rob(nums, 1, nums.length));
    }
    
    public int rob(int[] nums, int start, int end) {
        int prevMax = 0;
        int currMax = 0;
        for (int i = start; i < end; i++) {
            int num = nums[i];
            // prevMax + num => take curr
            // currMax => do not take curr
            int temp = currMax;
            currMax = Math.max(prevMax + num, currMax);
            prevMax = temp;
        }
        
        return currMax;
    }
}
