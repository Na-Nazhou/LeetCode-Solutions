class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None] * n for _ in range(m)]
        self.m = m
        self.n = n
        dp[-1][-1] = 1
        return self.helper(0, 0, dp)
        
    def helper(self, i, j, dp):
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return 0
        
        if dp[i][j] is not None:
            return dp[i][j]
        
        dircs = [[1, 0], [0, 1]]
        
        dp[i][j] = 0
        for di, dj in dircs:
            dp[i][j] += self.helper(i + di, j + dj, dp)
            
        return dp[i][j]