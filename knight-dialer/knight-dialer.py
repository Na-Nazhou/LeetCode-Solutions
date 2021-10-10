class Solution:
    def knightDialer(self, n: int) -> int:
        adj_list = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        
        memo = {}
        
        def dfs(pos, count):
            count -= 1
            if count == 0:
                return 1
            
            if (pos, count) in memo:
                return memo[(pos, count)]
            
            ans = 0
            for neighbor in adj_list[pos]:
                ans += dfs(neighbor, count)
            
            memo[(pos, count)] = ans
            return ans
        
        ans = 0
        for i in range(10):
            ans += dfs(i, n)
        
        return ans % (10 ** 9 + 7)