class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        counts = [0] * 32
        for num in nums:
            ptr = 0
            while num > 0:
                if num % 2 == 1:
                    counts[ptr] += 1
                num = num // 2
                ptr += 1
        
        ans = 0
        for count in counts:
            ans += count * (len(nums) - count)
        
        return ans