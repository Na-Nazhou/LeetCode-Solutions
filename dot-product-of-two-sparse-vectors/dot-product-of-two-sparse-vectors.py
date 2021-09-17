class SparseVector:
    def __init__(self, nums: List[int]):
        self.data = []
        for i, num in enumerate(nums):
            if nums != 0:
                self.data.append((i, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        i = 0
        j = 0
        res = 0
        
        while i < len(self.data) and j < len(vec.data):
            if self.data[i][0] == vec.data[j][0]:
                res += self.data[i][1] * vec.data[j][1]
                i += 1
                j += 1
            elif self.data[i][0] < vec.data[j][0]:
                i += 1
            else:
                j += 1
        
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)