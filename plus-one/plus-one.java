class Solution {
    public int[] plusOne(int[] digits) {
        int carry = 1;
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] + carry >= 10) {
                digits[i] = 0;
            } else {
                digits[i] += carry;
                carry = 0;
                break;
            }
        }
        
        
        if (carry == 0) {
            return digits;
        } else {
            int[] res = new int[digits.length + 1];
            res[0] = 1;
            for (int i = 1; i < res.length; i++) {
                res[i] = digits[i - 1];
            }
            return res;
        }
    }
}
