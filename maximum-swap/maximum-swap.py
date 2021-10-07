class Solution:
    def maximumSwap(self, num: int) -> int:
        
        num = list(str(num))
        curr_max = -1
        curr_max_idx = None
        swap = None
        
        for i in range(len(num) - 1, -1, -1):
            digit = int(num[i])
            if digit > curr_max:
                curr_max = digit
                curr_max_idx = i
            elif digit < curr_max:
                swap = [i, curr_max_idx]
        
        if swap is None:
            return int("".join(num))
        
        num[swap[0]], num[swap[1]] = num[swap[1]], num[swap[0]]
        
        return int("".join(num))