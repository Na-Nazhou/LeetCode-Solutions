class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = defaultdict(int)
        curr_sum = 0
        prefix_sum_count[curr_sum] += 1
        
        ans = 0
        for num in nums:
            curr_sum += num
            complement = curr_sum - k
            ans += prefix_sum_count[complement]
            prefix_sum_count[curr_sum] += 1
        
        return ans