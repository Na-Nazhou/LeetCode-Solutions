class Solution:
    def customSortString(self, order: str, s: str) -> str:
        pq = []
        ordering = defaultdict(int)
        for i, c in enumerate(order):
            ordering[c] = i
        
        for c in s:
            heapq.heappush(pq, (ordering[c], c))
        
        res = []
        while pq:
            _, c = heapq.heappop(pq)
            res.append(c)
        
        return "".join(res)