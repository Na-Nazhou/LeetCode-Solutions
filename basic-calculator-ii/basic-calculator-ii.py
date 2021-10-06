class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr_num = 0
        prev_op = "+"
        for i, c in enumerate(s):
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            if c in ['+', '-', '*', '/'] or i == len(s) - 1: 
                if prev_op == '+':
                    stack.append(curr_num) 
                if prev_op == '-':
                    stack.append(-curr_num)
                if prev_op == '*':
                    stack.append(stack.pop() * curr_num)
                if prev_op == "/":
                    stack.append(int(stack.pop() / curr_num))
                curr_num = 0
                prev_op = c
        
        return sum(stack)
                    