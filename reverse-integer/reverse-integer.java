class Solution {
    public int reverse(int x) {
        long answer = 0;
        while (x != 0) {
            int lsd = x % 10;
            x /= 10;
            answer = answer * 10 + lsd;
        }
        if (answer > Integer.MAX_VALUE || answer < Integer.MIN_VALUE) {
            return 0;
        } else {
            return (int) answer;
        }
    }
}
