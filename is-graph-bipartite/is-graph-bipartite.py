class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}
        
        def bfs(start):
            q = deque()
            q.append(start)
            visited[start] = 0
            color = 1
            while q:
                size = len(q)
                for _ in range(size):
                    node = q.popleft()
                    for neighbor in graph[node]:
                        if neighbor in visited:
                            if visited[neighbor] != color:
                                return False
                            continue

                        visited[neighbor] = color
                        q.append(neighbor)
                color = (color + 1) % 2
            
            return True
            
        for i in range(len(graph)):
            if i not in visited:
                if not bfs(i):
                    return False
        
        return True