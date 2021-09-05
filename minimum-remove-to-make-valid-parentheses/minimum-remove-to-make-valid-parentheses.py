class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = []
        for i, c in enumerate(s):
            if c != '(' and c != ')':
                res.append(c)
            if c == '(':
                stack.append(len(res))
                res.append(c)
            if c == ')':
                if not stack:
                    continue
                stack.pop()
                res.append(c)
        
        stack = set(stack)
        ans = []
        for i, c in enumerate(res):
            if i in stack:
                continue
            ans.append(c)
        return "".join(ans)