class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_zeros = 0
        start = 0
        end = 0
        ans = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                num_zeros += 1
            
            if num_zeros <= k:
                ans = max(ans, end - start + 1)
            else:
                if nums[start] == 0:
                    num_zeros -= 1
                start += 1
        return ans
                