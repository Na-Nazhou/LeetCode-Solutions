class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj_list = defaultdict(list)
        L = len(beginWord)
        
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                adj_list[pattern].append(word)
        
        print(adj_list)
        
        visited = set()
        q = Deque()
        q.append(beginWord)
        visited.add(beginWord)
        
        level = 1
        while q:
            size = len(q)
            for _ in range(size):
                word = q.popleft()
                for i in range(L):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neighbor in adj_list[pattern]:
                        if neighbor == endWord:
                            return level + 1
                        if neighbor in visited:
                            continue

                        visited.add(neighbor)
                        q.append(neighbor)
            level += 1
        
        return 0