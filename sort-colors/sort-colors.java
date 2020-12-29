class Solution {
    public void sortColors(int[] nums) {
        // [0, p1) => 0
        // [p1, p2] => 1
        // (p2, n) => 2
        int p1 = 0;
        int p2 = nums.length - 1;
        int curr = 0;
        
        while (curr <= p2) {
            int color = nums[curr];
            if (color == 0) {
                swap(curr++, p1++, nums);
            } 
            
            if (color == 1) {
                curr++;
            }
            
            if (color == 2) {
                swap(curr, p2--, nums);
            }
        }
    }
    
    private void swap(int i, int j, int[] arr) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
