class Solution {
    public int rob(int[] nums) {
        int prevMax = 0;
        int currMax = 0;
        for (int num : nums) {
            // prevMax + num => take curr
            // currMax => do not take curr
            int temp = currMax;
            currMax = Math.max(prevMax + num, currMax);
            prevMax = temp;
        }
        
        return currMax;
    }
}
