class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for i in range(len(s) - 1, -1, -1):
            found = False
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDict and dp[j]:
                    found = True
                    break
            if found:
                dp[i] = True
        return dp[0]
                    