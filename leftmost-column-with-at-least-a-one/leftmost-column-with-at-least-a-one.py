# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        r, c = binaryMatrix.dimensions()
    
        def leftMostColWithOneInRow(row):
            start = 0
            end = c - 1
            while start <= end:
                mid = (start + end) // 2
                if binaryMatrix.get(row, mid) == 0:
                    start = mid + 1
                else:
                    if mid == 0 or binaryMatrix.get(row, mid - 1) == 0:
                        return mid
                    else:
                        end = mid - 1
            
            return None
        
        ans = None
        for row in range(r):
            col = leftMostColWithOneInRow(row)
            if col is None:
                continue
            if ans is None:
                ans = c
            ans = min(ans, col)
        
        if ans is None:
            return -1
        else:
            return ans