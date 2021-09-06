class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        n = len(nums)
        
        i = 0
        while count < n:
            curr_idx = i
            curr_num = nums[curr_idx]
            while True:
                next_idx = (curr_idx + k) % n
                next_num = nums[next_idx]
                nums[next_idx] = curr_num
                curr_num = next_num
                curr_idx = next_idx
                count += 1
                
                if curr_idx == i:
                    break
            
            i += 1
                