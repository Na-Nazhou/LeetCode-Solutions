class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.helper(nums, [], ans)
        return ans
    
    def helper(self, nums, curr, ans):
        if len(curr) == len(nums):
            ans.append(curr[:])
            return
        
        for num in nums:
            if num in curr:
                continue
            
            curr.append(num)
            self.helper(nums, curr, ans)
            curr.pop()