class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            return s == s[::-1]
        
        start = 0
        end = len(s) - 1
        while start < end:
            c1 = s[start]
            c2 = s[end]
            if c1 != c2:
                return isPalindrome(s[start:end]) or isPalindrome(s[start + 1:end + 1])
            start += 1
            end -= 1
        
        return True
        
        