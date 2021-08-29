class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int m = heights.length;
        int n = heights[0].length;
        boolean[][] visitedByPacific = new boolean[m][n];
        boolean[][] visitedByAtlantic = new boolean[m][n];
        
        for (int i = 0; i < m; i++) {
            if (!visitedByPacific[i][0]) {
                dfs(i, 0, heights, visitedByPacific);
            }
            
            if (!visitedByAtlantic[i][n - 1]) {
                dfs(i, n - 1, heights, visitedByAtlantic);
            }
        }
        
        for (int j = 0; j < n; j++) {
            if (!visitedByPacific[0][j]) {
                dfs(0, j, heights, visitedByPacific);
            }
            
            if (!visitedByAtlantic[m - 1][j]) {
                dfs(m - 1, j, heights, visitedByAtlantic);
            }
        }
        
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (visitedByPacific[i][j] && visitedByAtlantic[i][j]) {
                    ans.add(List.of(i, j));
                }
            }
        }
        
        return ans;
    }
    
    private void dfs(int i, int j, int[][] heights, boolean[][] visited) {
        int m = heights.length;
        int n = heights[0].length;
        
        visited[i][j] = true;
        
        int[][] dirs = new int[][]{
            {0, 1},
            {0, -1},
            {1, 0},
            {-1, 0},
        };
        
        for (int[] dir : dirs) {
            int newI = i + dir[0];
            int newJ = j + dir[1];
            
            if (newI < 0 || newI >= m || newJ < 0 || newJ >= n) {
                continue;
            }
            if (visited[newI][newJ]) {
                continue;
            }
            if (heights[i][j] > heights[newI][newJ]) {
                continue;
            }
            
            dfs(newI, newJ, heights, visited);
        }
    }
}