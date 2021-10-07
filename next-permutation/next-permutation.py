class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        pos = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pos = i
                break
        
        if pos != -1:
            for i in range(len(nums) - 1, pos, -1):
                if nums[i] > nums[pos]:
                    nums[pos], nums[i] = nums[i], nums[pos]
                    break
        
        to_reverse = nums[pos + 1:]
        nums[pos + 1:] = to_reverse[::-1]
        