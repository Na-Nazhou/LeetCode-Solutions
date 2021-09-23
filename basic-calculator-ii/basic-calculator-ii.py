class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        
        prev = 0
        op = '+'
        curr = 0
        
        # Imagine we add a "0+" at the front of the expression
        
        for i, c in enumerate(s):
            if c.isdigit():
                curr = curr * 10 + int(c)
            
            if not c.isdigit() and not c.isspace() or i == len(s) - 1:
                if op == "+":
                    res += prev
                    prev = curr
                if op == "-":
                    res += prev
                    prev = -curr
                if op == "*":
                    prev *= curr
                if op == "/":
                    prev = int(prev / curr)
                op = c
                curr = 0
            
            print(c, res, prev, op, curr)
        
        res += prev
        print(prev, op, curr)
        return res