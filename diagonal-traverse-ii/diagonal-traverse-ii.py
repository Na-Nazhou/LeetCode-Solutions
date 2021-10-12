class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonal_map = defaultdict(list)
        max_diagonal = 0
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(nums[i]) - 1, -1, -1):
                diagonal = i + j
                diagonal_map[diagonal].append(nums[i][j])
                max_diagonal = max(max_diagonal, diagonal)
        
        res = []
        for i in range(max_diagonal + 1):
            res += diagonal_map[i]
        
        return res