class Solution:
    def minWindow(self, s: str, t: str) -> str:
        expected_freq = defaultdict(int)
        for c in t:
            expected_freq[c] += 1
        expected_completed = len(expected_freq)
            
        actual_freq = defaultdict(int)
        completed = 0
        start = 0
        ans = [None, None]
        min_length = None
        end = 0
        for end in range(len(s)):
            c = s[end]
            actual_freq[c] += 1
            if actual_freq[c] == expected_freq[c]:
                completed += 1
            
            while completed == expected_completed:
                length = end - start + 1
                if min_length is None or length < min_length:
                    ans = [start, end]
                    min_length = length
                
                to_remove = s[start]
                if actual_freq[to_remove] == expected_freq[to_remove]:
                    completed -= 1
                actual_freq[to_remove] -= 1
                start += 1
        
        if min_length is None:
            return ""
        
        return s[ans[0]:ans[1] + 1]
        