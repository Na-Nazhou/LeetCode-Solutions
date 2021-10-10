class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1
            
            while start < end:
                curr_sum = nums[i] + nums[start] + nums[end]
                if curr_sum == target:
                    return target
                
                if abs(curr_sum - target) < abs(res - target):
                    res = curr_sum
                
                if curr_sum < target:
                    start += 1
                else:
                    end -= 1
        
        return res
                    
                
            