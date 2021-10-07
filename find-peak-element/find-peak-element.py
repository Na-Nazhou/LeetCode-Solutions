class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if mid > 0 and nums[mid] < nums[mid - 1]:
                end = mid - 1
            
            elif mid < len(nums) -1 and nums[mid] < nums[mid + 1]:
                start = mid + 1
            
            else:
                return mid
        
        raise ValueError()