class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        if len(nums) == 0:
            return ans
        
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        
        if nums[start] != target:
            return ans
        
        ans[0] = start
        end = len(nums) - 1
        
        while start < end:
            mid = (start + end + 1) // 2
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid
        ans[1] = start
        
        return ans