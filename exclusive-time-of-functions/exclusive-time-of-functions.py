class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        def parse_log(log):
            params = log.split(":")
            f_id = int(params[0])
            event = params[1]
            ts = int(params[2])
            return f_id, event, ts
        
        res = [0] * n
        stack = []
        prev_ts = None
        for log in logs:
            f_id, event, ts = parse_log(log)
            
            if event == "start":
                if stack:
                    prev_f = stack[-1]
                    res[prev_f] += ts - prev_ts
                stack.append(f_id)
                prev_ts = ts
            if event == "end":
                prev_f = stack.pop()
                res[prev_f] += ts - prev_ts + 1
                prev_ts = ts + 1
        
        return res
                