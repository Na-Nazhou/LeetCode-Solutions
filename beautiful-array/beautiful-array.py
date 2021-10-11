class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        memo = {}
        memo[1] = [1]
        
        def helper(n):
            if n in memo:
                return memo[n]
            
            odd = helper((n + 1) // 2)
            even = helper(n // 2)
            memo[n] = [2 * i - 1 for i in odd] + [2 * i for i in even]
            return memo[n]
        
        return helper(n)
        