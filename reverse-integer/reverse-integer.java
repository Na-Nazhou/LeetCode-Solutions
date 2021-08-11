class Solution {
    public int reverse(int x) {
        int val = Math.abs(x);
        int curr = 0;
        boolean isPositive = x >= 0;
        
        while (val > 0) {
            int digit = val % 10;
            
            if (isPositive) {
                if (curr > (Integer.MAX_VALUE - digit) / 10) {
                    return 0;
                }
                curr = curr * 10 + digit;
            } else {
                if (curr < (Integer.MIN_VALUE + digit) / 10) {
                    return 0;
                }
                curr = curr * 10 - digit;
            }
            
            val = val / 10;
        }
        
        return curr;
    }
}