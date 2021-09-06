class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        count = 0
        m = defaultdict(int)
        m[0] = 1
        
        for num in nums:
            curr_sum += num
            count += m[curr_sum - k]
            m[curr_sum] += 1
        
        return count