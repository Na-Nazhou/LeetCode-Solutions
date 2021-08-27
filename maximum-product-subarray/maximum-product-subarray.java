class Solution {
    public int maxProduct(int[] nums) {
        int ans = nums[0];
        int prevMax = nums[0];
        int prevMin = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];            
            int currMax = Collections.max(List.of(num * prevMax, num * prevMin, num));
            int currMin = Collections.min(List.of(num * prevMax, num * prevMin, num));
            ans = Collections.max(List.of(ans, currMax, currMin));
            prevMax = currMax;
            prevMin = currMin;
        }
        
        return ans;
    }
}