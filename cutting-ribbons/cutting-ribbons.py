class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        start = 1
        end = sum(ribbons) // k
        
        while start < end:
            mid = (start + end + 1) // 2
            
            # Check if it is possible to get k ribbons of length `mid`
            count = 0
            for ribbon in ribbons:
                count += ribbon // mid
            if count < k:
                end = mid - 1
            else:
                start = mid
        
        if start == end:
            return start
        
        return 0