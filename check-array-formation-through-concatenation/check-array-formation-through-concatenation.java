class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        boolean[] used = new boolean[pieces.length];
        int i = 0;
        while (i < arr.length) {
            boolean matched = false;
            
            for (int j = 0; j < used.length; j++) {
                if (used[j]) {
                    continue;
                }
                
                int[] piece = pieces[j]; 
                if (piece[0] != arr[i]) {
                    continue;
                }
                
                for (int k = 0; k < piece.length; k++) {
                    if (piece[k] != arr[i + k]) {
                        return false;
                    }
                }
                
                used[j] = true;
                i += piece.length;
                matched = true;
                break;
            }
            
            if (!matched) {
                return false;
            }
        }
        
        return true;
    }
}
