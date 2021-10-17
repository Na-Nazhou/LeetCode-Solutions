class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        missing_ranges = []
        
        def add_range(start, end):
            if start > end:
                return
            
            if start == end:
                missing_ranges.append(str(start))
            else:
                missing_ranges.append(f'{start}->{end}')
        
        if not nums:
            add_range(lower, upper)
            return missing_ranges
        
        add_range(lower, nums[0] - 1)
        for i in range(1, len(nums)):
            prev = nums[i - 1]
            curr = nums[i]
            
            start = max(lower, prev + 1)
            end = min(upper, curr - 1)
            add_range(start, end)
        add_range(nums[-1] + 1, upper)
        
        return missing_ranges