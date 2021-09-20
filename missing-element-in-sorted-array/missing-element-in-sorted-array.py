class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            curr_missing = self.missingSoFar(nums, mid)
            if mid == end:
                next_missing = k
            else:
                next_missing = self.missingSoFar(nums, mid+1)
            
            if curr_missing < k and next_missing >= k:
                return nums[mid] + k - curr_missing
            
            if next_missing < k:
                start = mid + 1
            if curr_missing >= k:
                end = mid - 1
        
            
    def missingSoFar(self, nums, idx):
        return nums[idx] - nums[0] - idx