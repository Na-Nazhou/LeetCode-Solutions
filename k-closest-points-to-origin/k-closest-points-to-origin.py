class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x, y in points:
            distance = -1 * sqrt(x ** 2 + y ** 2)
            heapq.heappush(h, (distance, [x, y]))
            if len(h) > k:
                heapq.heappop(h)
        
        ans = []
        while h:
            pt = heapq.heappop(h)[1]
            ans.append(pt)
        
        return ans