class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        
        visited = []
        for i in range(self.m):
            row = []
            for j in range(self.n):
                row.append(False)
            visited.append(row)
        
        for i in range(self.m):
            for j in range(self.n):
                if word[0] == self.board[i][j]:
                    if self.dfs(i, j, word, 0, visited):
                        return True
        
        return False
    
    def dfs(self, i, j, word, idx, visited):
        if idx >= len(word):
            return True
        
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return False
        
        if self.board[i][j] != word[idx]:
            return False
        
        if visited[i][j] is True:
            return False
        
        visited[i][j] = True
        
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        
        found = False
        for direction in dirs:
            newI = i + direction[0]
            newJ = j + direction[1]
            
            result = self.dfs(newI, newJ, word, idx + 1, visited)
            
            if result is True:    
                found = True
                break
        
        visited[i][j] = False
        return found