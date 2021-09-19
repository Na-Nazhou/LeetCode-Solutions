class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            curr = s[i]
            if res and res[-1] == curr:
                res.pop()
            else:
                res.append(curr)
        
        return "".join(res)