class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        # [(-1, 'a')]
        pq = [(-count, c) for c, count in counts.items() ] # max heap
        heapq.heapify(pq) # O(n) - n: number of distinct characters
        
        ans = [] # ['a', 'b', 'a']
        freezed = None # [0, 'b']
        while pq:
            neg_count, c = heapq.heappop(pq)
            ans.append(c)
            neg_count += 1
            
            if freezed is not None and freezed[0] < 0:
                heapq.heappush(pq, freezed)
            
            freezed = (neg_count, c)
        
        if freezed[0] < 0:
            return ""
        
        return "".join(ans)
        