class Solution {
    // Time complexity: O(n)
    // Space complexity: O(1)
    
    public int maxProfit(int[] prices) {
        int currMinPrice = Integer.MAX_VALUE;
        int currMaxProfit = Integer.MIN_VALUE;
        
        for (int price : prices) {
            if (price > currMinPrice) {
                currMaxProfit = Math.max(currMaxProfit, price - currMinPrice);
            } else {
                currMinPrice = Math.min(currMinPrice,  price);
            }
        }
        
        return Math.max(currMaxProfit, 0);
    }
}