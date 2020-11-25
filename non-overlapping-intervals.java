class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals.length == 0) {
            return 0;
        }
        
        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[1], i2[1]));
        
        int count = 1;
        int curr = intervals[0][1];
        for (int[] interval : intervals) {
            if (interval[0] >= curr) {
                curr = interval[1];
                count++;
                continue;
            }
        }
        
        return intervals.length - count;
    }
}
