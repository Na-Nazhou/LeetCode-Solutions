class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[0], i2[0]));
        
        for (int i = 1; i < intervals.length; i++) {
            int prevEnd = intervals[i - 1][1];
            int currStart = intervals[i][0];
            if (currStart < prevEnd) {
                return false;
            }
        }
        
        return true;
    }
}
