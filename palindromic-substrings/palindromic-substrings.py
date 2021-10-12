class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        def helper(i):
            nonlocal count
            left = i
            right = i
            
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    count += 1
                    left -=1
                    right += 1
                else:
                    break
            
            left = i
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    count += 1
                    left -=1
                    right += 1
                else:
                    break
        
        for i in range(len(s)):
            helper(i)
        
        return count
            