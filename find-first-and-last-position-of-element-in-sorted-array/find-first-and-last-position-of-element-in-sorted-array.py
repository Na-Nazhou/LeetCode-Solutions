class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        
        first_occurrence = None
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                if mid == 0 or nums[mid - 1] != target:
                    first_occurrence = mid
                    break
                else:
                    end = mid - 1
        
        if first_occurrence is None:
            return [-1, -1]
        
        start = 0
        end = len(nums) - 1
        
        last_occurrence = None
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    last_occurrence = mid
                    break
                else:
                    start = mid + 1
        
        return [first_occurrence, last_occurrence]