class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        m = len(grid)
        n = len(grid[0])
        
        start = (0, 0)
        end = (m - 1, n - 1)
        
        q = deque()
        q.append(start)
        visited = set()
        visited.add(start)
        
        length = 1
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                if (x, y) == end:
                    return length
                
                dircs = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
                for dx, dy in dircs:
                    new_x = x + dx
                    new_y = y + dy
                    
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
                        continue
                    
                    if (new_x, new_y) in visited:
                        continue
                    
                    if grid[new_x][new_y] != 0:
                        continue
                    
                    visited.add((new_x, new_y))
                    q.append((new_x, new_y))
            
            length += 1
        
        return -1