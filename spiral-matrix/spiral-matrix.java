class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ans = new ArrayList<>();
        
        if (matrix == null || matrix.length == 0) {
            return ans;
        }
        
        int m = matrix.length;
        int n = matrix[0].length;
        
        int top = 0;
        int bottom = m -1;
        int left = 0;
        int right = n -1;
        while (top <= bottom && left <= right) {
            for (int i = left; i <= right; i++) {
                ans.add(matrix[top][i]);
            }
            
            for (int i = top + 1; i <= bottom - 1; i++) {
                ans.add(matrix[i][right]);
            }
            
            if (top < bottom) {
                for (int i = right; i >= left; i--) {
                    ans.add(matrix[bottom][i]);
                }
            }
            
            if (left < right) {
                for (int i = bottom - 1; i >= top + 1; i--) {
                    ans.add(matrix[i][left]);
                }
            }
            
            top++;
            bottom--;
            left++;
            right--;
        }
       
        return ans;
    }
}
