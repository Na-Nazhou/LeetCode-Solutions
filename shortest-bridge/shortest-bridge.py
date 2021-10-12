class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def get_neighbors(i, j):
            dircs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            res = []
            for di, dj in dircs:
                new_i = i + di
                new_j = j + dj
                if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                    continue
                res.append((new_i, new_j))
            return res
            
        q = deque()
        visited = [[False] * n for _ in range(m)]
        def dfs(i, j):
            visited[i][j] = True
            q.append((i, j))
            for new_i, new_j in get_neighbors(i, j):
                if visited[new_i][new_j]:
                    continue
                
                if grid[new_i][new_j] != 1:
                    continue
                
                dfs(new_i, new_j)
        
        for i in range(m):
            found_island = False
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found_island = True
                    break
            if found_island:
                break
        
        print(visited)
        
        length = 0
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for new_i, new_j in get_neighbors(i, j):
                    if visited[new_i][new_j]:
                        continue
                    
                    visited[new_i][new_j] = True
                    if grid[new_i][new_j] == 1:
                        return length
                    
                    q.append((new_i, new_j))
                    
            length += 1
        
        raise ValueError("Unexpected")
                
                 