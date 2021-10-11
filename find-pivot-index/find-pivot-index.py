class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            prefix_sum.append(curr_sum)
        
        for i, _ in enumerate(nums):
            if i == 0:
                left = 0
            else:
                left = prefix_sum[i - 1]
            
            right = prefix_sum[-1] - prefix_sum[i]
            
            if left == right:
                return i
        
        return -1
        
        