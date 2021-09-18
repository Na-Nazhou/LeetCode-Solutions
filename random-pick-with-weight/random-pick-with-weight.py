class Solution:

    def __init__(self, w: List[int]):
        self.arr = []
        self.total = 0
        for x in w:
            self.total += x
            self.arr.append(self.total)

    def pickIndex(self) -> int:
        x = random.randint(1, self.total)
        start = 0
        end = len(self.arr) - 1
        while start <= end:
            mid = (start + end) // 2
            
            if self.arr[mid] < x:
                start = mid + 1
            else:
                if mid == 0 or self.arr[mid - 1] < x:
                    return mid
                else:
                    end = mid - 1
        
        raise ValueError("Invalid")


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()