class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = {}
        in_degree = defaultdict(int)
        
        # IMPORTANT!!!
        if len(words) == 1:
            return "".join(list(set(list(words[0]))))
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            foundDiff = False
            ptr1 = 0
            ptr2 = 0
            while ptr1 < len(word1) and ptr2 < len(word2):
                c1 = word1[ptr1]
                c2 = word2[ptr2]
                ptr1 += 1
                ptr2 += 1
                
                if c1 not in g:
                    g[c1] = []
                if c2 not in g:
                    g[c2] = []
                    
                if c1 == c2:
                    continue
                
                foundDiff = True
                g[c1].append(c2)
                in_degree[c2] += 1
                break
            
            if not foundDiff and len(word1) > len(word2):
                return ""
            
            while ptr1 < len(word1):
                c = word1[ptr1]
                if c not in g:
                    g[c] = []
                ptr1 += 1
                print(c)
            
            while ptr2 < len(word2):
                c = word2[ptr2]
                if c not in g:
                    g[c] = []
                ptr2 += 1
                print(c)

        q = deque()
        res = []
        for v in g.keys():
            if in_degree[v] == 0:
                q.append(v)
        
        while q:
            v = q.popleft()
            res.append(v)
            for neighbor in g[v]:                    
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
                
        if len(res) != len(g.keys()):
            return ""
        
        return "".join(res)