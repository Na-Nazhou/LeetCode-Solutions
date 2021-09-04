class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])
        
        for curr in intervals[1:]:
            if free_rooms[0] <= curr[0]:
                heapq.heappop(free_rooms)
            
            heapq.heappush(free_rooms, curr[1])
        
        return len(free_rooms)