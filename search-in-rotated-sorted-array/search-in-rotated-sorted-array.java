class Solution {
    public int search(int[] nums, int target) {
        int n = nums.length;
        int left = 0;
        int right = n - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < nums[right]) {
                right = mid;
            } else {
                left = mid + 1; 
            }
        }
        
        int start = left;
        left = 0;
        right = n - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int midVal = nums[(mid + start) % n];
            if (midVal == target) {
                return (mid + start) % n;
            }
            
            if (midVal > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
            
        }
        
        return -1;
    }
}
