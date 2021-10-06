class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        bal = 0 # number of unclosed open brackets
        min_add = 0 # number of missing open brackets
        for c in s:
            if c == '(':
                bal += 1
            if c == ')':
                if bal == 0:
                    min_add += 1
                else:
                    bal -= 1
        
        return min_add + bal