class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        res = []
        for c in order:
            if c in counts:
                for _ in range(counts[c]):
                    res.append(c)
                del counts[c]
        
        for c, count in counts.items():
            for _ in range(count):
                res.append(c)
        
        return "".join(res)
            