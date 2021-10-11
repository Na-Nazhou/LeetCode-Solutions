class Solution:
    def myAtoi(self, s: str) -> int:
        is_negative = False
        curr = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c == '-':
                is_negative = True
                i += 1
                break
                
            if c == '+':
                i += 1
                break
                
            if c.isdigit():
                break
            
            if c == ' ':
                i += 1
            else:
                break
        
        while i < len(s):
            c = s[i]
            if c.isdigit():
                curr = curr * 10 + int(c)
            else:
                break
            
            i += 1
        
        if is_negative:
            curr = -curr
        
        curr = min(curr, 2 ** 31 - 1)
        curr = max(curr, -2 ** 31)
        
        return curr