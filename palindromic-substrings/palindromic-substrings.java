class Solution {
    public int countSubstrings(String s) {
        int n = s.length();
        boolean[][] dp = new boolean[n][n];
        int count = 0;
        for (int i = n - 1; i >= 0; i--) {
            char a = s.charAt(i);
            for (int j = i; j < n; j++) {
                char b = s.charAt(j);
                
                if (i == j) {
                    dp[i][j] = true;
                } else if (a == b) {
                    if (j == i + 1) {
                        dp[i][j] = true;
                    } else if (dp[i + 1][j - 1]) {
                        dp[i][j] = true;
                    }
                }
                
                if (dp[i][j]) {
                    count += 1;
                }
            }
        }
        
        return count;
    }
}