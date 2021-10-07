class Solution:
    def trap(self, height: List[int]) -> int:
        left_right_max = [[0, 0] for _ in range(len(height))]
        curr_max = 0
        for i in range(len(height)):
            h = height[i]
            curr_max = max(curr_max, h)
            left_right_max[i][0] = curr_max
        
        curr_max = 0
        for i in range(len(height) - 1, -1, -1):
            h = height[i]
            curr_max = max(curr_max, h)
            left_right_max[i][1] = curr_max
        
        ans = 0
        for i, (left_max, right_max) in enumerate(left_right_max):
            ans += min(left_max, right_max) - height[i]
            
        return ans
        
        