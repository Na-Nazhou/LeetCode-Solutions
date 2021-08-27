class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[0], i2[0]));
        
        ArrayList<int[]> res = new ArrayList<>();
        int[] prevInterval = intervals[0];
        for (int i = 1; i < intervals.length; i++) {
            int[] interval = intervals[i];
            if (interval[0] <= prevInterval[1]) {
                prevInterval[1] = Math.max(prevInterval[1], interval[1]);
            } else {
                res.add(prevInterval);
                prevInterval = interval;
            }
        }
        res.add(prevInterval);
        
        int[][] ans = new int[res.size()][2];
        for (int i = 0; i < res.size(); i++) {
            ans[i] = res.get(i);
        }
        
        return ans;
    }
}