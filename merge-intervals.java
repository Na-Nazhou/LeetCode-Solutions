class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) {
            return intervals;
        }
        
        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[0], i2[0]));
        
        List<int[]> result = new LinkedList<>();
        int[] currInterval = intervals[0];
        
        for (int[] interval : intervals) {
            if (interval[1] >= currInterval[0] && interval[0] <= currInterval[1]) {
                currInterval[0] = Math.min(currInterval[0], interval[0]);
                currInterval[1] = Math.max(currInterval[1], interval[1]);
            } else {
                result.add(currInterval);
                currInterval = interval;
            }
        }
        
        result.add(currInterval);
        
        return result.toArray(new int[result.size()][2]);
    }
}
