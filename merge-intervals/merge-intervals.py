class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        
        ans = [intervals[0]]
        
        for i in range(1, len(intervals)):
            prev = ans[-1]
            curr = intervals[i]
            
            if prev[1] >= curr[0]:
                prev[1] = max(prev[1], curr[1])
            else:
                ans.append(curr)
            
        return ans