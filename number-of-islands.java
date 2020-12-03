class Solution {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }
        
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] visited = new boolean[m][n];
        
        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j] && grid[i][j] == '1') {
                    dfs(i, j, visited, grid);
                    ans += 1;
                }
                
            }
        }
        
        return ans;
    }
    
    private void dfs(int x, int y, boolean[][] visited, char[][] grid) {
        visited[x][y] = true;
        
        visit(x - 1, y, visited, grid);
        visit(x + 1, y, visited, grid);
        visit(x, y - 1, visited, grid);
        visit(x, y + 1, visited, grid);
    }
    
    private void visit(int x, int y, boolean[][] visited, char[][] grid) {
        if (x < 0 || x >= grid.length || y < 0 || y >= grid[0].length) {
            return;
        }
        
        // Check if it is visited before or it is water
        if (visited[x][y] || grid[x][y] == '0') {
            return;
        }
        
        dfs(x, y, visited, grid);
    }
}
