class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ptr_a = len(a) - 1
        ptr_b = len(b) - 1
        res = []
        while ptr_a >= 0 or ptr_b >= 0 or carry != 0:
            curr = 0
            if ptr_a >= 0:
                curr += int(a[ptr_a])
                ptr_a -= 1
            if ptr_b >= 0:    
                curr += int(b[ptr_b])
                ptr_b -= 1
            
            curr += carry
            carry = curr // 2
            curr = curr % 2
            
            res.append(str(curr))
        
        return "".join(res[::-1])
            
        
            