class Solution {
    public int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];
        int top = 0;
        int bottom = n -1;
        int left = 0;
        int right = n -1;
        
        int curr = 1;
        while (top <= bottom && left <= right) {
            for (int i = left; i <= right; i++) {
                matrix[top][i] = curr;
                curr++;
            }
            
            for (int i = top + 1; i <= bottom - 1; i++) {
                matrix[i][right] = curr;
                curr++;
            }
            
            if (top < bottom) {
                for (int i = right; i >= left; i--) {
                    matrix[bottom][i] = curr;
                    curr++;
                }
            }
            
            if (left < right) {
                for (int i = bottom - 1; i >= top + 1; i--) {
                    matrix[i][left] = curr;
                    curr++;
                }
            }
            
            top++;
            bottom--;
            left++;
            right--;
        }
        
        return matrix;
    }
}
