class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        bal = 0
        ans = []
        
        # Remove extra closing brackets
        for c in s:
            if c == ')' and bal == 0:
                continue
            
            if c == '(':
                bal += 1
                
            if c == ')':
                bal -= 1
            
            ans.append(c)
        
        s = "".join(ans)
        bal = 0
        ans = []
        
        # Remove extra open brackets
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c == '(' and bal == 0:
                continue
            
            if c == ')':
                bal += 1
            
            if c == '(':
                bal -= 1
            
            ans.append(c)
                
        ans.reverse()
        return "".join(ans)