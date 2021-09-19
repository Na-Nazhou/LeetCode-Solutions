class Solution:

    def __init__(self, nums: List[int]):
        self.m = defaultdict(list)
        for i, num in enumerate(nums):
            self.m[num].append(i)

    def pick(self, target: int) -> int:
        choices = self.m[target]
        idx = random.randint(0, len(choices) - 1)
        return choices[idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)