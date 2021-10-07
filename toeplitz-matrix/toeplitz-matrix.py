class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        def check_diagonal(i, j):
            val = matrix[i][j]
            while i < m and j < n:
                if matrix[i][j] != val:
                    return False
                i += 1
                j += 1
            return True
        
        for i in range(m):
            if not check_diagonal(i, 0):
                return False
        
        for j in range(1, n):
            if not check_diagonal(0, j):
                return False
        
        return True