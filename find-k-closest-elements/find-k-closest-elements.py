class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start = 0
        end = len(arr) - 1
        while end - start + 1 > k:
            a = arr[start]
            b = arr[end]
            
            if abs(a - x) < abs(b - x):
                end -= 1
            elif abs(a - x) == abs(b - x) and a < b:
                end -= 1
            else:
                start += 1
        
        return arr[start:end+1]