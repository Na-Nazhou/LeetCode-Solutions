class Solution:

    def __init__(self, nums: List[int]):
        self.map = {}
        for i, num in enumerate(nums):
            if num not in self.map:
                self.map[num] = []
            self.map[num].append(i)
            

    def pick(self, target: int) -> int:
        if target not in self.map:
            raise ValueError()
        
        options = self.map[target]
        idx = random.randint(0, len(options) -1)
        return options[idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)