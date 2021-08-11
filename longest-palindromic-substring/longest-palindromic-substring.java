class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        boolean[][] dp = new boolean[n][n];
        int currMax = 0;
        int currStart = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            char c1 = s.charAt(i);
            for (int j = i; j < s.length(); j++) {
                char c2 = s.charAt(j);
                boolean isPalindrome = false;
                if (i == j) {
                    isPalindrome = true;
                } else if (i + 1 == j && c1 == c2) {
                    isPalindrome = true;
                } else if (dp[i + 1][j - 1] && c1 == c2) {
                    isPalindrome = true;
                }
                
                if (isPalindrome) {
                    dp[i][j] = true;
                    if (j - i + 1 > currMax) {
                        currMax = j - i + 1;
                        currStart = i;    
                    }
                }
               
            }
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < currMax; i++) {
            sb.append(s.charAt(currStart + i));
        }
        
        return sb.toString();
    }
}