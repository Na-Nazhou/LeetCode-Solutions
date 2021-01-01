class Solution {
    private static final int[][] dir = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    
    public int numIslands(char[][] grid) {
        
        int m = grid.length;
        int n = grid[0].length;
        int count = 0;
        boolean[][] visited = new boolean[m][n]; 
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    dfs(i, j, visited, grid);
                    count++;
                }
            }
        }
        
        return count;
    }
    
    private void dfs(int i, int j, boolean[][] visited, char[][] grid) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length) {
            return;
        }
        
        if (grid[i][j] == '0') {
            return;
        }
        
        if (visited[i][j]) {
            return;
        }
        
        visited[i][j] = true;
        
        for (int[] neighbor : dir) {
            dfs(i + neighbor[0], j + neighbor[1], visited, grid);
        }
    }
}
