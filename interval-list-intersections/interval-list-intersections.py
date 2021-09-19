class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            i1 = firstList[i]
            i2 = secondList[j]
            if i1[0] <= i2[1] and i1[1] >= i2[0]:
                start = max(i1[0], i2[0])
                end = min(i1[1], i2[1])
                ans.append([start, end])
            
            if i1[1] <= i2[1]:
                i += 1
            
            if i2[1] <= i1[1]:
                j += 1
        
        return ans