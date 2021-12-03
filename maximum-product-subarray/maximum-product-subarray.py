class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        ans = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            temp = max_product
            max_product = max(max_product * num, min_product * num, num)
            min_product = min(temp * num, min_product * num, num)
            ans = max(ans, max_product, min_product)
        
        return ans
        