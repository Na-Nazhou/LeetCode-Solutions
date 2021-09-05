# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        start = 1
        end = n
        while start <= end:
            mid = start + (end - start) // 2
            if not isBadVersion(mid):
                start = mid + 1
                continue
            
            if mid > 1 and isBadVersion(mid - 1):
                end = mid - 1
            else:
                return mid
        
        raise ValueError("No bad version found")
            
        