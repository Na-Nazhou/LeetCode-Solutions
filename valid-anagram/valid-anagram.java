class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        int[] letters = new int[26];
        for (char ch : s.toCharArray()) {
            int idx = ch - 'a';
            letters[idx]++;
        }
        
        for (char ch : t.toCharArray()) {
            int idx = ch - 'a';
            letters[idx]--;
            if (letters[idx] < 0) {
                return false;
            }
        }
        
        return true;
    }
}
