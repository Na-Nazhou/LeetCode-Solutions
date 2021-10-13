class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        increasing = None
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                if increasing is False:
                    return False
                if increasing is None:
                    increasing = True
            elif nums[i - 1] > nums[i]:
                if increasing is True:
                    return False
                if increasing is None:
                    increasing = False
        
        return True