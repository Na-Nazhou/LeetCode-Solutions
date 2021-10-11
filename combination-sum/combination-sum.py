class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        def backtrack(i, curr, seq):
            if curr > target:
                return
            
            if curr == target:
                ans.append(seq[:])
                return
            
            if i == len(candidates):
                return
            
            for j in range(i, len(candidates)):
                seq.append(candidates[j])
                backtrack(j, curr + candidates[j], seq)
                seq.pop()
        
        backtrack(0, 0, [])
        
        return ans