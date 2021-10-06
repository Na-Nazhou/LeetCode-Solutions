class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i1 = len(num1) - 1
        i2 = len(num2) - 1
        
        ans = []
        carry = 0
        while i1 >= 0 or i2 >= 0 or carry > 0:
            sum = carry
            
            if i1 >= 0:
                sum += ord(num1[i1]) - ord('0')
                i1 -= 1
                
            if i2 >= 0:
                sum += ord(num2[i2]) - ord('0')
                i2 -= 1
            
            ans.append(str(sum % 10))
            carry = sum // 10
        
        ans.reverse()
        
        return "".join(ans)
                