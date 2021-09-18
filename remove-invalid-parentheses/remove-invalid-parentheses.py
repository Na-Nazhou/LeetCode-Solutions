class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.res = set()
        
        bal = 0
        right_rem = 0
        for c in s:
            if c == '(':
                bal += 1
            if c == ')':
                if bal == 0:
                    right_rem += 1
                if bal > 0:
                    bal -= 1
        left_rem = bal
        
        self.backtrack(s, 0, 0, left_rem, right_rem, [])
            
        return self.res
        
    def backtrack(self, s, i, bal, left_rem, right_rem, curr):
        if i == len(s):
            if bal == 0:
                self.res.add("".join(curr))
            return
        
        c = s[i]
        
        # Ignore current bracket if possible
        if c == '(' and left_rem > 0:
            self.backtrack(s, i + 1, bal, left_rem - 1, right_rem, curr)
        
        if c == ')' and right_rem > 0:
            self.backtrack(s, i + 1, bal, left_rem, right_rem - 1, curr)
        
        # Include current char
        curr.append(c)
        
        if c == '(':
            self.backtrack(s, i + 1, bal + 1, left_rem, right_rem, curr)
        elif c == ')':
            if bal > 0:
                self.backtrack(s, i + 1, bal - 1, left_rem, right_rem, curr)
        else:
            self.backtrack(s, i + 1, bal, left_rem, right_rem, curr)
                
        curr.pop()