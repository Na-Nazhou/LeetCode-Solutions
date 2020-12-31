class Solution {
    public int titleToNumber(String s) {
        int curr = 0;
        for (char ch : s.toCharArray()) {
            int n = ch - 'A' + 1;
            curr = curr * 26 + n;
        }
        return curr;
    }
}
