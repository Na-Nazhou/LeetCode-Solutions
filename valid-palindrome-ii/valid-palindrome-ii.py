class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                remove_left = s[start+1:end+1]
                remove_right = s[start:end]
                return remove_left == remove_left[::-1] or remove_right == remove_right[::-1]
        return True