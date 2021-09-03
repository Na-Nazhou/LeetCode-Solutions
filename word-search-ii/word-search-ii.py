class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False
    
    def insertWord(self, word):
        curr = self
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.eow = True

class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()
        
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        self.ans = []
        
        for word in words:
            self.root.insertWord(word)
        
        self.visited = [[False] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                self.dfs(i, j, self.root, [])
        
        return self.ans
    
    def dfs(self, i, j, parent, word):
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return
        
        if self.visited[i][j] is True:
            return
        
        c = self.board[i][j]
        if c not in parent.children:
            return
        
        self.visited[i][j] = True
        word.append(c)
        
        child = parent.children[c]
        if child.eow:
            self.ans.append(''.join(word))
            child.eow = False
        
        # Optimization
        if len(child.children) == 0:
            del parent.children[c]
        
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        
        for di, dj in dirs:
            newI = i + di
            newJ = j + dj
            self.dfs(newI, newJ, child, word)
        
        word.pop()
        self.visited[i][j] = False