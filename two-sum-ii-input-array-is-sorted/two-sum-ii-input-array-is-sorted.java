class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;
        
        while (left < right) {
            int currSum = numbers[left] + numbers[right];
            if (currSum > target) {
                right--;
            } else if (currSum < target) {
                left++;
            } else {
                return new int[]{left + 1, right + 1};
            }
        }
        
        throw new IllegalArgumentException("No solution found");
    }
}