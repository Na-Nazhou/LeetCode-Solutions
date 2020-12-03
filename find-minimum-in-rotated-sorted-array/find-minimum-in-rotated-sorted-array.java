class Solution {
    public int findMin(int[] nums) {
        int n = nums.length;
        if (n == 1) {
            return nums[0];
        }
        
        int left = 0;
        int right = nums.length - 1;
        
        // Not rotated
        if (nums[left] < nums[right]) {
            return nums[left];
        }
        left++;
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[0]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        return nums[left];
    }
}
