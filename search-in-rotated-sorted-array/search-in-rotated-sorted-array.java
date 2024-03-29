class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        
        boolean isOnLeft = target >= nums[0];
        
        while (left <= right) {
            int mid = (left + right) / 2;
            int num = nums[mid];
            if (num == target) {
                return mid;
            }
            
            if (isOnLeft) {
                if (num < target) {
                    if (num >= nums[0]) {
                        left = mid + 1;
                    } else {
                        right = mid - 1;
                    }
                } else {
                    right = mid - 1;
                }
            } else {
                if (num < target) {
                    left = mid + 1;
                } else {
                    if (num >= nums[0]) {
                        left = mid + 1;
                    } else {
                        right = mid - 1;
                    }
                }
            }
        }
        
        return -1;
    }
}