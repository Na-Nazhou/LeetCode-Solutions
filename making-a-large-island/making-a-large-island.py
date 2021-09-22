class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        num_of_islands = 0
        size_map = defaultdict(int) # key: label, value: size
        island_map = {} # key: pos, value: label
        m = len(grid)
        n = len(grid[0])
        
        def within_bound(i, j):
            return i >= 0 and i < m and j >= 0 and j < n
        
        def dfs(i, j, label, visited):
            visited[i][j] = True
            size_map[label] += 1
            island_map[(i, j)] = label
            
            for di, dj in dirs:
                new_i = i + di
                new_j = j + dj
                if within_bound(new_i, new_j) and grid[new_i][new_j] == 1 and not visited[new_i][new_j]:
                    dfs(new_i, new_j, label, visited)
        
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    dfs(i, j, num_of_islands, visited)
                    num_of_islands += 1
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    area = 1
                    labels = set()
                    for di, dj in dirs:
                        new_i = i + di
                        new_j = j + dj
                        if (new_i, new_j) in island_map:
                            label = island_map[(new_i, new_j)]
                            if label not in labels:
                                area += size_map[label]
                                labels.add(label)
                    max_area = max(max_area, area)
        
        if max_area == 0:
            return max(size_map.values())
        else:
            return max_area