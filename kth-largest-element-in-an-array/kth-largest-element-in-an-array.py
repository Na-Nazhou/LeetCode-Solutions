class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quick_select(nums, 0, len(nums) - 1, k - 1)
        return nums[k - 1]
        
    def quick_select(self, nums, start, end, k):
        if start == end:
            return
        
        pivot_idx = random.randint(start, end)
        pivot_idx = self.partition(nums, start, end, pivot_idx)
        if pivot_idx == k:
            return
        if pivot_idx < k:
            self.quick_select(nums, pivot_idx + 1, end, k)
        else:
            self.quick_select(nums, start, pivot_idx - 1, k)
        
    def partition(self, nums, start, end, pivot_idx):
        self.swap(nums, start, pivot_idx)
        pivot = nums[start]
        ptr = start
        for i in range(start + 1, end + 1):
            if nums[i] > pivot:
                ptr += 1
                self.swap(nums, ptr, i)
        self.swap(nums, start, ptr)
        return ptr
        
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]