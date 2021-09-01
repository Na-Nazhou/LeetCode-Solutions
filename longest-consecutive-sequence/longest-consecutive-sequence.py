class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
        
        ans = 0
        
        for num in s:
            if num - 1 not in s: # potential start of a consecutive sequence
                curr = num + 1
                
                while curr in s:
                    curr += 1
                
                ans = max(ans, curr - num)
        
        return ans
                