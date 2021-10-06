class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        component_size = defaultdict(int) # key: component_id, size of the component
        
        m = len(grid)
        n = len(grid[0])
        
        visited = [ [False] * n for _ in range(m) ]
        components = [ [None] * n for _ in range(m) ]
        
        def dfs(i, j, component_id):
            visited[i][j] = True
            
            component_size[component_id] += 1
            components[i][j] = component_id
            
            dircs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for di, dj in dircs:
                new_i = i + di
                new_j = j + dj
                
                if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                    continue
                
                if visited[new_i][new_j]:
                    continue
                
                if grid[new_i][new_j] != 1:
                    continue
                    
                dfs(new_i, new_j, component_id)
            
        
        curr_component_id = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    dfs(i, j, curr_component_id)
                    curr_component_id += 1
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    size = 1
                    dircs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                    components_set = set()
                    for di, dj in dircs:
                        new_i = i + di
                        new_j = j + dj

                        if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                            continue
                        
                        if grid[new_i][new_j] != 1:
                            continue
                        
                        component_id = components[new_i][new_j]
                        if component_id not in components_set:
                            components_set.add(component_id)
                            size += component_size[component_id]
                        
                    max_area = max(max_area, size)
                else:
                    component_id = components[i][j]
                    size = component_size[component_id]
                    max_area = max(max_area, size)
        
        return max_area
                        