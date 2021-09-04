class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        visited = [False] * n
        self.dfs(g, 0, visited)
        
        return all(node is True for node in visited)
        
    def dfs(self, g, start, visited):
        if visited[start]:
            return
        
        visited[start] = True
        
        for end in g[start]:
            self.dfs(g, end, visited)