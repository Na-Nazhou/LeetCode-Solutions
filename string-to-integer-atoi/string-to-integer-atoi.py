class Solution:
    def myAtoi(self, s: str) -> int:
        curr = 0
        is_negative = False
        i = 0
        while i < len(s):
            c = s[i]
            if c == " ":
                i += 1
                continue
            break
        
        if i < len(s):
            if s[i] in ["+", "-"]:
                if s[i] == "-":
                    is_negative = True
                i += 1
        
        while i < len(s):
            c = s[i]
            if not c.isdigit():
                break
            
            curr = curr * 10 + int(c)
            if curr >= 2 ** 31:
                break
            
            i += 1
        
        if is_negative:
            return max(-2 ** 31, -curr)
        else:
            return min(2 ** 31 - 1, curr)
            
            