class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.rob_simple(nums, 0, len(nums) - 2), self.rob_simple(nums, 1, len(nums) - 1))
    
    def rob_simple(self, nums, start, end):
        t1 = 0
        t2 = 0
        for i in range(start, end + 1):
            temp = t1
            t1 = max(t2 + nums[i], t1)
            t2 = temp
        
        return t1