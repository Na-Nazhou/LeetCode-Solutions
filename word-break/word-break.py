class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dictionary = set(wordDict)
        
        dp = [False] * len(s)
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in dictionary and (j == len(s) or dp[j]):
                    dp[i] = True
                    break
        
        return dp[0]