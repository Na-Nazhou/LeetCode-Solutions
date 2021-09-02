class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target)
    
    def helper(self, nums, target):
        if target < 0:
            return 0
        
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        
        return dp[target]