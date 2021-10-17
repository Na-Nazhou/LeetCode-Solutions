class SparseVector:
    def __init__(self, nums: List[int]):
        self.list = []
        for i, num in enumerate(nums):
            if num != 0:
                self.list.append((i, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        list1 = self.list
        list2 = vec.list
        ptr1 = 0
        ptr2 = 0
        ans = 0
        while ptr1 < len(list1) and ptr2 < len(list2):
            pair1 = list1[ptr1]
            pair2 = list2[ptr2]
            
            if pair1[0] < pair2[0]:
                ptr1 += 1
                continue
            
            if pair2[0] < pair1[0]:
                ptr2 += 1
                continue
            
            ans += pair1[1] * pair2[1]
            ptr1 += 1
            ptr2 += 1
        
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)