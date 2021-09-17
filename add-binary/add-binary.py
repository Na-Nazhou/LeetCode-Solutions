class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry > 0:
            digit = carry
            if i >= 0:
                digit += int(a[i])
                i -= 1
            if j >= 0:
                digit += int(b[j])
                j -= 1
            
            carry = digit // 2
            digit = digit % 2
            res.append(str(digit))
        
        return "".join(res[::-1])