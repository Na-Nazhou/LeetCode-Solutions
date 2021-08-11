class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {        
        if (nums1.length > nums2.length) {
            return findMedianSortedArraysHelper(nums2, nums1);
        } else {
            return findMedianSortedArraysHelper(nums1, nums2);
        }
        
    }
    
    private double findMedianSortedArraysHelper(int[] nums1, int[] nums2) {
        int start = 0;
        int end = nums1.length;
        
        while (start <= end) {
            int i = (start + end) / 2;
            int j = (nums1.length + nums2.length + 1) / 2 - i;
            
            if (i > 0 && nums1[i - 1] > nums2[j]) {
                end = i - 1;
            } else if (i < nums1.length && nums2[j - 1] > nums1[i]) {
                start = i + 1;
            } else {
                int leftMax, rightMin;
                if (i == 0) {
                    leftMax = nums2[j - 1];
                } else if (j == 0) {
                    leftMax = nums1[i - 1];
                } else {
                    leftMax = Math.max(nums1[i - 1], nums2[j - 1]);
                }

                if ((nums1.length + nums2.length) % 2 == 1) {
                    return leftMax;
                }

                if (i == nums1.length) {
                    rightMin = nums2[j];
                } else if (j == nums2.length) {
                    rightMin = nums1[i];
                } else {
                    rightMin = Math.min(nums1[i], nums2[j]);
                }

                return (leftMax + rightMin) / 2.0;
            }
        }
        
        
        throw new IllegalArgumentException("Unknown error");
    }
}