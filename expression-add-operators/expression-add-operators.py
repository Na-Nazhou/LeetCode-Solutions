class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        
        def backtrack(i, prev, curr, result, expr):
            nonlocal ans
            
            if i == len(num):
                if curr == 0 and result == target:
                    ans.append("".join(expr))
                return
            
            digit = int(num[i])
            
            curr = curr * 10 + digit
            curr_str = str(curr)
            
            if curr > 0:
                # NO-OP
                backtrack(i + 1, prev, curr, result, expr)
            
            if not expr:
                expr.append(curr_str)
                backtrack(i + 1, curr, 0, result + curr, expr)
                expr.pop()
                return
            
            # Addition
            expr.append("+")
            expr.append(curr_str)
            backtrack(i + 1, curr, 0, result + curr, expr)
            expr.pop()
            expr.pop()

            # Subtraction
            expr.append("-")
            expr.append(curr_str)
            backtrack(i + 1, -curr, 0, result - curr, expr)
            expr.pop()
            expr.pop()

            # Multiplication (IMPORTANT!!!)
            expr.append("*")
            expr.append(curr_str)
            backtrack(i + 1, curr * prev, 0, result - prev + prev * curr, expr)
            expr.pop()
            expr.pop()
            
        backtrack(0, 0, 0, 0, [])
        
        return ans
                
                