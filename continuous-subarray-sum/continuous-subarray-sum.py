class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = {}
        curr = 0
        s[curr] = -1
        for i, num in enumerate(nums):
            curr = (curr + num) % k
            if curr in s:
                if s[curr] != i - 1:
                    return True
            else:
                s[curr] = i
        return False