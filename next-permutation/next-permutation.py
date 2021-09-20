class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        first_decrease = None
        for i in range(len(nums) - 1, 0, -1):
            prev = nums[i - 1]
            curr = nums[i]
            
            if prev < curr:
                first_decrease = i - 1
                break
        
        if first_decrease is None:
            nums.reverse()
            return
        
        
        for i in range(len(nums) - 1, first_decrease, -1):
            if nums[i] > nums[first_decrease]:
                nums[i], nums[first_decrease] = nums[first_decrease], nums[i]
                break
                
        nums[first_decrease + 1:] = reversed(nums[first_decrease + 1:])