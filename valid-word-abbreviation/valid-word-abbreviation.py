class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        word_ptr = 0
        abbr_ptr = 0
        while abbr_ptr < len(abbr) and word_ptr < len(word):
            print(abbr_ptr, word_ptr)
            
            c = abbr[abbr_ptr]
            if not c.isdigit():
                if c != word[word_ptr]:
                    return False
                
                abbr_ptr += 1
                word_ptr += 1
                continue
            
            curr = 0
            while abbr_ptr < len(abbr):
                c = abbr[abbr_ptr]
                if not c.isdigit():
                    break
                
                digit = int(c)
                if curr == 0 and digit == 0: # leading zero
                    return False
                
                curr = curr * 10 + digit
                abbr_ptr += 1
            
            word_ptr += curr
        
        return abbr_ptr == len(abbr) and word_ptr == len(word)
                
            
            