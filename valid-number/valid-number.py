class Solution:
    def isNumber(self, s: str) -> bool:
        if "e" not in s and "E" not in s:
            return self.isDecimalNumber(s) or self.isInteger(s)
        
        if "e" in s:
            parts = s.split("e")
        if "E" in s:
            parts = s.split("E")
            
        if len(parts) != 2:
            return False
        
        return self.isInteger(parts[1]) and (self.isDecimalNumber(parts[0]) or self.isInteger(parts[0]))
        
    def isDecimalNumber(self, s):
        if len(s) == 0:
            return False
        
        i = 0
        if s[0] == "+" or s[0] == "-":
            i += 1
        
        if i == len(s) - 1:
            return False
        
        foundDot = False
        while i < len(s):
            if s[i] == ".":
                if foundDot:
                    return False
                foundDot = True
                i += 1
                continue
            
            if not s[i].isdigit():
                return False
            
            i += 1
        return foundDot
    
    def isInteger(self, s: str) -> bool:
        if len(s) == 0:
            return False
        
        i = 0
        if s[0] == "+" or s[0] == "-":
            i += 1
        
        if i == len(s):
            return False
        
        while i < len(s):
            if not s[i].isdigit():
                return False
            
            i += 1
        
        return True
    