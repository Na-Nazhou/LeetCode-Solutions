class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for start, end in edges:
            g[start].append(end)
            g[end].append(start)
        
        visited = [False] * n
        ans = 0
        for i in range(n):
            if visited[i] is False:
                self.dfs(g, i, visited)
                ans += 1 
        
        return ans
        
    def dfs(self, g, start, visited):
        if visited[start]:
            return
        
        visited[start] = True
        
        for end in g[start]:
            self.dfs(g, end, visited)
            