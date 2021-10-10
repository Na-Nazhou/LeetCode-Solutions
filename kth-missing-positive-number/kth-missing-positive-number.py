class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def get_num_of_missing(i):
            if i == len(arr):
                return float("inf")
            
            return arr[i] - i - 1
        
        start = 0
        end = len(arr)
        while start < end:
            mid = (start + end) // 2
            if get_num_of_missing(mid) < k:
                start = mid + 1
            else:
                end = mid
        
        # arr[start - 1] + (k - get_num_of_missing(start - 1))
        # arr[start - 1] + (k - arr[start - 1] + start + 1 - 1)
        return k + start
                