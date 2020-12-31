class Solution {
    public void moveZeroes(int[] nums) {
        int p = 0;
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (num != 0) {
                int temp = nums[p];
                nums[p] = num;
                nums[i] = temp;
                p++;
            } 
        }
    }
}
