class Solution:
    def compress(self, chars: List[str]) -> int:
        ptr = 0
        curr_count = 0
        for i in range(len(chars)):
            curr_count += 1
            if i < len(chars) - 1 and chars[i] == chars[i + 1]:
                continue
            
            chars[ptr] = chars[i]
            ptr += 1
            if curr_count > 1:
                for digit in list(str(curr_count)):
                    chars[ptr] = digit
                    ptr += 1
            curr_count = 0
        
        return ptr
                