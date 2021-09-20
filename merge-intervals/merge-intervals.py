class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda i:i[0])
        for curr in intervals:
            if not res:
                res.append(curr)
                continue
            
            prev = res[-1]
            if prev[1] >= curr[0]:
                prev[1] = max(prev[1], curr[1])
            else:
                res.append(curr)
        
        return res
            