class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = [] 
        self.combinationSumHelper(candidates, 0, target, [])
        return self.ans
    
    def combinationSumHelper(self, candidates, i, target, combi):
        if target == 0:
            self.ans.append(combi[:])
            return
        
        if i >= len(candidates) or target < 0:
            return
        

        self.combinationSumHelper(candidates, i + 1, target, combi)
        
        combi.append(candidates[i])
        self.combinationSumHelper(candidates, i, target - candidates[i], combi)
        combi.pop()