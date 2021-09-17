class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        m = defaultdict(int) # key: sum; value: count
        curr_sum = 0
        ans = 0
        # IMPORTANT!!!
        m[0] = 1
        for num in nums:
            curr_sum += num
            ans += m[curr_sum-k]
            m[curr_sum] += 1
        
        return ans
        