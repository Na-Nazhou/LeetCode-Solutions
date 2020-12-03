class Solution {
    private char[][] board;
    private char[] word;
    private int m;
    private int n;
    private int[][] dir = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    public List<String> findWords(char[][] board, String[] words) {
        List<String> res = new ArrayList<>();
        Map<Character, List<int[]>> map = new HashMap<>();
        
        this.board = board;
        this.m = board.length;
        this.n = board[0].length;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char ch = board[i][j];
                map.putIfAbsent(ch, new ArrayList<>());
                map.get(ch).add(new int[]{i, j});
            }
        }
        
        for (String word : words) {
            this.word = word.toCharArray();
            char firstChar = this.word[0];
            if (!map.containsKey(firstChar)) {
                continue;
            }
            for (int[] pos : map.get(firstChar)) {
                if (search(pos[0], pos[1], 0)) {
                    res.add(word);
                    break;
                }
            }
        }
        
        return res;
    }
    
    // Start search for word[k..] from board[i, j]
    private boolean search(int i, int j, int k) {
        if (k == word.length) {
            return true;
        }
        
        if (i < 0 || i >= m || j < 0 || j >= n) {
            return false;
        }
        
        // Must not visit again on this path
        if (board[i][j] == '*') {
            return false;
        }
        
        if (board[i][j] != word[k]) {
            return false;
        }
        
        // Mark as visited
        board[i][j] = '*';
        
        for (int[] pos : dir) {
            if (search(i + pos[0], j + pos[1], k + 1)) {
                board[i][j] = word[k];
                return true;  
            } 
        }
        
        // Backtrack and unmark visit
        board[i][j] = word[k];
        return false;
    }
}
