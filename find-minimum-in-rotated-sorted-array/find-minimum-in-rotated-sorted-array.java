class Solution {
    public int findMin(int[] nums) {
        int left = 1;
        int right = nums.length - 1;
        
        // Not rotated
        if (nums[0] <= nums[right]) {
            return nums[0];
        }
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int num = nums[mid];
            if (num < nums[mid - 1]) {
                return num;
            }
            if (num >= nums[0]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        throw new IllegalArgumentException("Error");
    }
}