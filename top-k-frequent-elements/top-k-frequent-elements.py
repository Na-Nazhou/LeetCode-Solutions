class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        h = [] # min heap
        
        for num, count in counts.items():
            heappush(h, (count, num))
            if len(h) > k:
                heappop(h)
        
        ret = [ num for _, num in h ]
        
        return ret