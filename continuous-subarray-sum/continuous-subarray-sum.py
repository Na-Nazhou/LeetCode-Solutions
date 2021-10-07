class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_modulo = {}
        prefix_modulo[0] = -1
        curr_modulo = 0
        for i, num in enumerate(nums):
            curr_modulo = (curr_modulo + num) % k
            if curr_modulo in prefix_modulo and prefix_modulo[curr_modulo] < i - 1:
                return True
            if curr_modulo not in prefix_modulo:
                prefix_modulo[curr_modulo] = i
        
        return False