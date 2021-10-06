class Solution:

    def __init__(self, w: List[int]):
        self.arr = []
        curr_sum = 0
        for num in w:
            curr_sum += num
            self.arr.append(curr_sum)

    def pickIndex(self) -> int:
        index = random.randint(1, self.arr[-1])
        # Find the first integer that is >= index
        start = 0
        end = len(self.arr) - 1
        while start < end:
            mid = (start + end) // 2
            if self.arr[mid] < index:
                start = mid + 1
            else:
                end = mid
        
        return start
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()