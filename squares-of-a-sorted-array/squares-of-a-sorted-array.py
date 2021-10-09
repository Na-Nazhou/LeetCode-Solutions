class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        min_abs = float('inf')
        start = None
        for i in range(len(nums)):
            if abs(nums[i]) <= min_abs:
                min_abs = abs(nums[i])
                start = i
            else:
                break
        
        ans = []
        ans.append(nums[start] ** 2)
        left = start - 1
        right = start + 1
        while left >= 0 and right < len(nums):
            if abs(nums[left]) <= abs(nums[right]):
                ans.append(nums[left] ** 2)
                left -= 1
            else:
                ans.append(nums[right] ** 2)
                right += 1
        
        while left >= 0:
            ans.append(nums[left] ** 2)
            left -= 1
        
        while right < len(nums):
            ans.append(nums[right] ** 2)
            right += 1
        
        return ans
        
        