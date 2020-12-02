class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] matrix) {
        List<List<Integer>> res = new ArrayList<>();
        
        if (matrix.length == 0) {
            return new ArrayList<>();
        }
        
        int m = matrix.length;
        int n = matrix[0].length;
        boolean[][] pacific = new boolean[m][n];
        boolean[][] atalantic = new boolean[m][n];
        
        for (int i = 0; i < m; i++) {
            pacific[i][0] = true;
            atalantic[i][n - 1] = true;
        }
        
        for (int i = 0; i < n; i++) {
            pacific[0][i] = true;
            atalantic[m - 1][i] = true;
        }
        
        for (int i = 0; i < m; i++) {
            dfs(i, 0, pacific, matrix);
            dfs(i, n - 1, atalantic, matrix);
        }
        
        for (int i = 0; i < n; i++) {
            dfs(0, i, pacific, matrix);
            dfs(m - 1, i, atalantic, matrix);
        }
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atalantic[i][j]) {
                    res.add(Arrays.asList(i, j));
                }
            }
        }
            
        return res;
    }
    
    private void dfs(int x, int y, boolean[][] visited, int[][] matrix) {
        int height = matrix[x][y];
        visit(x - 1, y, visited, matrix, height);
        visit(x + 1, y, visited, matrix, height);
        visit(x, y - 1, visited, matrix, height);
        visit(x, y + 1, visited, matrix, height);
    }
    
    private void visit(int x, int y, boolean[][] visited, int[][]matrix, int height) {
        if (x < 0 || x >= matrix.length || y < 0 || y >= matrix[0].length) {
            return;
        }
        
        if (matrix[x][y] >= height && !visited[x][y]) {
            visited[x][y] = true;
            dfs(x, y, visited, matrix);
        }
    }
}
