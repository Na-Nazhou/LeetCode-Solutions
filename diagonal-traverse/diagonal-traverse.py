class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonals[i + j].append(mat[i][j])
        
        ans = []
        for i, diagonal in diagonals.items():
            if i % 2 == 1:
                ans += diagonal
            else:
                ans += reversed(diagonal)
        
        return ans