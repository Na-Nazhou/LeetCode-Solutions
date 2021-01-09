class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            char leftChar = s.charAt(left);
            char rightChar = s.charAt(right);
            if (!Character.isAlphabetic(leftChar) && !Character.isDigit(leftChar)) {
                left++;
                continue;
            }
            
            if (!Character.isAlphabetic(rightChar) && !Character.isDigit(rightChar)) {
                right--;
                continue;
            }
            
            leftChar = Character.toLowerCase(leftChar);
            rightChar = Character.toLowerCase(rightChar);
            if (leftChar != rightChar) {
                return false;
            }
            
            left++;
            right--;
        }
        
        return true;
    }
}
