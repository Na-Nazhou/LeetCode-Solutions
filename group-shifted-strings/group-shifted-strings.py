class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for string in strings:
            h = []
            for i in range(1, len(string)):
                prev = string[i - 1]
                curr = string[i]
                gap = (ord(curr) - ord(prev) + 26) % 26
                h.append(gap)
            m[tuple(h)].append(string)
        
        return list(m.values())