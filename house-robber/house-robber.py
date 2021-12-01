class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [None] * len(nums)
        def helper(i):
            if i >= len(nums):
                return 0
            
            if memo[i] is not None:
                return memo[i]
            
            ans = max(nums[i] + helper(i + 2), helper(i + 1))
            memo[i] = ans
            return ans
        
        return helper(0)