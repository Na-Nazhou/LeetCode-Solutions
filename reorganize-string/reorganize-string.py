class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = defaultdict(int)
        max_count = 0
        max_char = None
        for c in s:
            counts[c] += 1
            if counts[c] > max_count:
                max_count = counts[c]
                max_char = c
        
        if max_count * 2 - 1 > len(s):
            return ""
        
        res = [None] * len(s)
        idx = 0
        while max_count > 0:
            res[idx] = max_char
            idx += 2
            max_count -= 1
        del counts[max_char]
        
        for c, count in counts.items():
            while count > 0:
                if idx >= len(s):
                    idx = 1
                res[idx] = c
                count -= 1
                idx += 2
        
        return "".join(res)
        