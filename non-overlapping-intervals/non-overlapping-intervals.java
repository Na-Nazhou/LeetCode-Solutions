class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        // Sort by end time
        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[1], i2[1]));
        
        int count = 0;
        int prev = 0;
        for (int curr = 1; curr < intervals.length; curr++) {
            int[] i1 = intervals[prev];
            int[] i2 = intervals[curr];
            
            if (i2[0] < i1[1]) {
                count += 1;
            } else {
                prev = curr;
            }
        }
        
        return count;
    }
}