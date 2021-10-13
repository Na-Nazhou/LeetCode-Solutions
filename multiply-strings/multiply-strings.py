class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        N = len(num1) + len(num2)
        ans = [0] * N
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        for p1, d1 in enumerate(num1):
            for p2, d2 in enumerate(num2):
                num_zeros = p1 + p2
                
                carry = ans[num_zeros]
                product = int(d1) * int(d2) + carry
                ans[num_zeros] = product % 10
                ans[num_zeros + 1] += product // 10
        
        while ans and ans[-1] == 0:
            ans.pop()
            
        if not ans:
            return '0'
        
        return ''.join(str(digit) for digit in reversed(ans))