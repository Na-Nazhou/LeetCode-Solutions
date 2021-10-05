class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        bal = 0
        s_without_extra_close_bracket = []
        for c in s:
            if c == '(':
                bal += 1
            elif c== ')':
                if bal == 0:
                    continue
                
                bal -= 1
            
            s_without_extra_close_bracket.append(c)
        
        if bal == 0:
            return "".join(s_without_extra_close_bracket)
        
        bal = 0
        s_without_extra_open_backet = []
        for i in range(len(s_without_extra_close_bracket) - 1, -1, -1):
            c = s_without_extra_close_bracket[i]
            if c == '(':
                if bal == 0:
                    continue
                    
                bal -= 1
            elif c== ')':
                bal += 1
            
            s_without_extra_open_backet.append(c)
        
        return "".join(s_without_extra_open_backet[::-1])

            
                
                    