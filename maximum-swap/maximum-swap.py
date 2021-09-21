class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [ int(c) for c in str(num)]
        
        # First a such that digits[a] < digits[a + 1]
        a = None
        for i in range(len(digits) - 1):
            curr = digits[i]
            next = digits[i + 1]
            if next > curr:
                a = i
                break
        
        if a is None:
            return num
        
        # Last b which is the maximum in digits[a+1:]
        b = a + 1
        for i in range(a + 2, len(digits)):
            if digits[i] >= digits[b]:
                b = i
        for i in range(a + 1):
            if digits[i] < digits[b]:
                digits[i], digits[b] = digits[b], digits[i]
                break
        
        res = 0
        for digit in digits:
            res = res * 10 + digit
        
        return res
        