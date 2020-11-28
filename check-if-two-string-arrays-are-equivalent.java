class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        int i = 0;
        int j = 0;
        
        int s1 = 0;
        int s2 = 0;
        
        while (s1 < word1.length && s2 < word2.length) {
            char char1 = word1[s1].charAt(i);
            char char2 = word2[s2].charAt(j);
            if (char1 != char2) {
                return false;
            } 
            
            if (i == word1[s1].length() - 1) {
                i = 0;
                s1++;
            } else {
                i++;
            }
            
            if (j == word2[s2].length() - 1) {
                j = 0;
                s2++;
            } else {
                j++;
            }
        }
        
        return s1 == word1.length && s2 == word2.length;
    }
}
