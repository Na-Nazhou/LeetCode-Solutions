class Solution {
    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        List<String> ans = new ArrayList<>();
        int next = lower;
        for (int num : nums) {
            if (num > next) {
                addRange(ans, next, num - 1);
            }
            next = num + 1;
        }
        
        if (next <= upper) {
            addRange(ans, next, upper);
        }
        
        return ans;
    }
    
    private void addRange(List<String> list, int start, int end) {
        if (start == end) {
            list.add(String.valueOf(start));
        } else {
            list.add(String.format("%d->%d", start, end));
        }
    }
}
