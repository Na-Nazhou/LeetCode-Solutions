class Solution {
    public int countArrangement(int n) {
        return countArrangement(n, 1, new boolean[n + 1]);
    }
    
    public int countArrangement(int n, int next, boolean[] used) {
        if (next == n + 1) {
            return 1;
        }
        
        int ans = 0;
        
        for (int i = 1; i <= n; i++) {
            if (used[i]) {
                continue;
            }
            
            if (i % next == 0 || next % i == 0) {
                used[i] = true;
                ans += countArrangement(n, next + 1, used);
                used[i] = false;
            } 
        }
        
        return ans;
    }
}
