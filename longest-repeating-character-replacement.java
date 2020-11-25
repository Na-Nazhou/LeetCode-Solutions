class Solution {
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
​
        int max = 0;
        int start = 0;
        for(int end = 0; end < s.length(); end++) {
            int endIdx = s.charAt(end) - 'A';
            count[endIdx]++;
                
            max = Math.max(max, count[endIdx]);
                
            if (max + k < end - start + 1) {
                int startIdx = s.charAt(start) - 'A';
                count[startIdx]--;
                start++;
            }
        }
        return s.length() - start;
    }
}
