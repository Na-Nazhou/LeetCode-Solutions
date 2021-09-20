class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        
        negatives = 0
        if dividend < 0:
            dividend = -dividend
            negatives += 1
            
        if divisor < 0:
            divisor = -divisor
            negatives += 1
        
        quotient = 0
        while divisor <= dividend:
            multiplier = 1 
            curr_sum = divisor
            while curr_sum < 2 ** 30 and curr_sum + curr_sum <= dividend:
                multiplier += multiplier
                curr_sum += curr_sum
            quotient += multiplier
            dividend -= curr_sum
        
        if negatives == 1:
            return -quotient
        else:
            return quotient