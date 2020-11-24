class Solution {
    public boolean isPalindrome(String s) {
        
        char[] charArr = s.toLowerCase().toCharArray();
        int i = 0;
        int j = charArr.length - 1;
        while (i < j) {
            char a = charArr[i];
            char b = charArr[j];
            
            if (!isAlphanumeric(a)) {
                i++;
                continue;
            }
            
            if (!isAlphanumeric(b)) {
                j--;
                continue;
            }
            
            if (a != b) {
                return false;
            }
                        
            i++;
            j--;
        }
        
        return true;
    }
    
    public boolean isAlphanumeric(char c) {
        return (c >= 'a' && c <= 'z') ||
           (c >= 'A' && c <= 'Z') ||
           (c >= '0' && c <= '9');
    }
}
