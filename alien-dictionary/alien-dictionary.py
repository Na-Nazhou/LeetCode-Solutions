class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_list = defaultdict(set)
        in_degree = {}
        for word in words:
            for c in word:
                in_degree[c] = 0
        
        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]
            
            foundDiff = False
            for c1, c2 in zip(first, second):
                if c1 != c2:
                    foundDiff = True
                    if c2 not in adj_list[c1]:
                        adj_list[c1].add(c2)
                        in_degree[c2] += 1
                    break
                    
            if len(first) > len(second) and not foundDiff:
                return ""
            
        output = []
        q = deque([c for c in in_degree if in_degree[c] == 0])
        while q:
            c1 = q.popleft()
            output.append(c1)
            for c2 in adj_list[c1]:
                in_degree[c2] -= 1
                if in_degree[c2] == 0:
                    q.append(c2)
        
        if len(output) < len(in_degree):
            return ""
        
        return "".join(output)