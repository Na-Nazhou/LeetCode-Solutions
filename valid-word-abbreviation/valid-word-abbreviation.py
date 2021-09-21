class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        length = 0
        for c in abbr:
            if c.isdigit():
                
                # Leading zero
                if length == 0 and int(c) == 0:
                    return False
                
                length = length * 10 + int(c)
            else:
                i += length
                length = 0
                if i >= len(word) or word[i] != c:
                    return False
                i += 1
        
        if length > 0:
            i += length
        
        return i == len(word)