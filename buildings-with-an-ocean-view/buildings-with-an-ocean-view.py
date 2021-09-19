class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        curr_max = -float("inf")
        for i in range(len(heights) - 1, -1, -1):
            height = heights[i]
            if height > curr_max:
                ans.append(i)
                curr_max = max(curr_max, height)
                
        ans.reverse()
        
        return ans