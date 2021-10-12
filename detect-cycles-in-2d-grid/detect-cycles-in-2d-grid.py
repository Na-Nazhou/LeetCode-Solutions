class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]
        
        def dfs(i, j, parent_i, parent_j):
            if visited[i][j] == 1:
                return True
            
            visited[i][j] = 1
            
            dircs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for di, dj in dircs:
                new_i = i + di
                new_j = j + dj
                if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                    continue
                
                if visited[new_i][new_j] == 2:
                    continue
                    
                if new_i == parent_i and new_j == parent_j:
                    continue
                
                if grid[new_i][new_j] != grid[i][j]:
                    continue
                
                print(i, j, new_i, new_j)
                if dfs(new_i, new_j, i, j):
                    return True
            
            visited[i][j] = 2
            
            return False
        
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0:
                    if dfs(i, j, None, None):
                        return True
        
        return False