class Solution {
    public int maxSubArray(int[] nums) {
        int prevMax = nums[0];
        int max = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];
            if (prevMax < 0) {
                prevMax = num;
            } else {
                prevMax += num;
            }
            max = Math.max(max, prevMax);
        }
        
        return max;
    }
}