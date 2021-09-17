class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        m = { c: i for i, c in enumerate(order) }
        for i in range(1, len(words)):
            word1 = words[i - 1]
            word2 = words[i]
            foundDiff = False
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    foundDiff = True
                
                if m[c1] > m[c2]:
                    return False
                if m[c1] < m[c2]:
                    break
            
            if not foundDiff and len(word1) > len(word2):
                return False
        
        return True
            
            
        