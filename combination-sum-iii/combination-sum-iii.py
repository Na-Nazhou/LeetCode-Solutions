class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        self.helper(k, 1, n, [])
        return self.ans
    
    def helper(self, k, i, n, combi):
        if n == 0 and len(combi) == k:
            self.ans.append(list(combi))
            return
        
        if i > 9 or n < 0 or len(combi) > k:
            return
        
        self.helper(k, i + 1, n, combi)
        combi.append(i)
        self.helper(k, i + 1, n - i, combi)
        combi.pop()
            