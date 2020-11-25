class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<Interval> result = new LinkedList<Interval>();
        int i = 0;
        while (i < intervals.length && intervals[i][1] < newInterval[0]) {
            result.add(new Interval(intervals[i]));
            i++;
        }
        
        int start = newInterval[0];
        int end = newInterval[1];
        
        while (i < intervals.length && intervals[i][0] <= newInterval[1]) {
            start = Math.min(start, intervals[i][0]);
            end = Math.max(end, intervals[i][1]);
            i++;
        }
        
        result.add(new Interval(start, end));
        
        while (i < intervals.length) {
            result.add(new Interval(intervals[i]));
            i++;
        }
        
        int[][] ans = new int[result.size()][2];
        int j = 0;
        for (Interval interval : result) {
            ans[j][0] = interval.start;
            ans[j][1] = interval.end;
            j++;
        }
        return ans;
    }
    
}
​
class Interval {
    int start;
    int end;
    
    Interval(int start, int end) {
        this.start = start;
        this.end = end;
    }
    
    Interval(int[] interval) {
        this.start = interval[0];
        this.end = interval[1];
    }
}
