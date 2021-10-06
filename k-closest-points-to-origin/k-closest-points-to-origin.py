class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = [] # max heap
        
        def distance(p):
            return sqrt(p[0] ** 2 + p[1] ** 2)
        
        for point in points:
            dist = distance(point)
            heapq.heappush(h, (-dist, point))
            if len(h) > k:
                heapq.heappop(h)
        
        ans = [pair[1] for pair in h]
        return ans
            
        