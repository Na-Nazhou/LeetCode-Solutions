class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = defaultdict(int)
        
        for c in s:
            counts[c] += 1
        
        foundOdd = False
        for c, count in counts.items():
            if count % 2 == 1:
                if foundOdd:
                    return False
                foundOdd = True
        
        return True