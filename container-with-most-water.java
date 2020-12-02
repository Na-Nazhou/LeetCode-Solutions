class Solution {
    public int maxArea(int[] height) {
        int currMax = 0;
        
        int i = 0;
        int j = height.length - 1;
        while (i < j) {
            int area = (j - i) * Math.min(height[i], height[j]);
            currMax = Math.max(currMax, area);
            
            if (height[i] > height[j]) {
                j--;
            } else {
                i++;
            }
        }
        
        return currMax;
    }
}
