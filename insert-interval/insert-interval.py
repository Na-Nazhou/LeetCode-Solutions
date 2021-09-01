class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        
        i = 0
        while i < len(intervals):
            if newInterval[0] < intervals[i][0]:
                break
            
            ans.append(intervals[i])
            i += 1
        
        # Insert newInterval
        if len(ans) == 0 or not self.is_overlap(ans[-1], newInterval):
            ans.append(newInterval)
        else:
            ans[-1] = self.merge(ans[-1], newInterval)
        
        while i < len(intervals):
            if self.is_overlap(ans[-1], intervals[i]):
                ans[-1] = self.merge(ans[-1], intervals[i])
            else:
                ans.append(intervals[i])
            i += 1
            
        return ans
    
    def is_overlap(self, i1, i2):
        return i1[0] <= i2[1] and i1[1] >= i2[0]
    
    def merge(self, i1, i2):
        if not self.is_overlap(i1, i2):
            return None
        
        start = min(i1[0], i2[0])
        end = max(i1[1], i2[1])
        return [start, end]
        