class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo = max(ceil(sum(weights) / days), max(weights))
        hi = sum(weights)
        
        def get_num_days(cap):
            num_days = 1
            curr_weight = 0
            for weight in weights:
                curr_weight += weight
                if curr_weight > cap:
                    num_days += 1
                    curr_weight = weight
            
            return num_days
        
        while lo < hi:
            mid = (lo + hi) // 2
            
            if get_num_days(mid) > days:
                lo = mid + 1
            else:
                hi = mid
        
        return lo
            
                    
        