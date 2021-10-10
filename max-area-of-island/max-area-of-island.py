class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        def dfs(i, j):
            visited[i][j] = True
            
            dircs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            count = 1
            for di, dj in dircs:
                new_i = i + di
                new_j = j + dj
                
                if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                    continue
                
                if grid[new_i][new_j] == 0:
                    continue
                
                if visited[new_i][new_j]:
                    continue
                
                count += dfs(new_i, new_j)
            
            return count
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area