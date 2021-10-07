class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        def parse_log(log):
            params = log.split(":")
            func_id = int(params[0])
            event = params[1]
            ts = int(params[2])
            
            return (func_id, event, ts)
        
        ans = [0] * n
        
        prev_ts = 0
        stack = []
        for log in logs:
            func_id, event, ts = parse_log(log)
            if event == "start":
                if stack:
                    prev_func_id = stack[-1]
                    ans[prev_func_id] += ts - prev_ts
                stack.append(func_id)
                prev_ts = ts
            
            if event == "end":
                prev_func_id = stack.pop() # assert prev_func_id == func_id
                ans[prev_func_id] += ts + 1 - prev_ts
                prev_ts = ts + 1
        
        return ans