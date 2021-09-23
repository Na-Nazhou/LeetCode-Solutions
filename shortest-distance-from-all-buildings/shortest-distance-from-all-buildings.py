class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        total_houses = 0
        house_reached = 0
        distances = []
        for i in range(m):
            distances.append([])
            for j in range(n):
                distances[-1].append([0, 0])
                if grid[i][j] == 1:
                    total_houses += 1

        def bfs(i, j):
            dircs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            visited = [[False] * n for _ in range(m)]
            q = deque()
            
            q.append(((i, j), 0))
            visited[i][j] = True
            while q:
                pos, dis = q.popleft()
                if grid[pos[0]][pos[1]] == 0:
                    distances[pos[0]][pos[1]][0] += dis
                    distances[pos[0]][pos[1]][1] += 1
                
                for di, dj in dircs:
                    new_i = pos[0] + di
                    new_j = pos[1] + dj
                    if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n: # out of bound
                        continue
                    if grid[new_i][new_j] != 0: # obstacle
                        continue
                    if visited[new_i][new_j]:
                        continue
                    visited[new_i][new_j] = True
                    q.append(((new_i, new_j), dis + 1))
            
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 0 and visited[i][j] and distances[i][j][1] != house_reached:
                        grid[i][j] = 2

            return float("inf")
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    house_reached += 1
                    bfs(i, j)
        
        min_dist = float("inf")
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and distances[i][j][1] == total_houses:
                    min_dist = min(min_dist, distances[i][j][0])
        
        if min_dist == float("inf"):
            return -1
        
        return min_dist