class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordering = {}
        for i, c in enumerate(order):
            ordering[c] = i
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            found_diff = False
            for c1, c2 in zip(word1, word2):
                if c1 == c2:
                    continue
                
                found_diff = True
                if ordering[c1] > ordering[c2]:
                    return False
                else:
                    break
            
            if not found_diff and len(word1) > len(word2):
                return False
        
        return True