class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        for i in range(len(s) - 1, -1, -1):
            if int(s[i]) == 0:
                continue
            
            dp[i] += dp[i + 1]
            if i < len(s) - 1 and (int(s[i]) == 1 or (int(s[i]) == 2 and int(s[i + 1]) <= 6)):
                dp[i] += dp[i + 2]
        
        return dp[0]