class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        ans = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            candidates = [max_product * num, min_product * num, num]
            max_product = max(candidates)
            min_product = min(candidates)
            ans = max(ans, max_product, min_product)
        
        return ans
        