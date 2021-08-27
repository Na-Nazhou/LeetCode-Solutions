class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();
        if (nums.length < 3) {
            return ans;
        }
        
        for (int i = 0; i < nums.length; i++) {
            int a = nums[i];
            if (i > 0 && nums[i - 1] == a) {
                continue;
            }
            
            Map<Integer, Integer> map = new HashMap<>();
            for (int j = i + 1; j < nums.length; j++) {
                int b = nums[j];
                int complement = -1 * a - b;
                int count = map.getOrDefault(b, 0);
                if (b != complement && map.containsKey(b)) {
                    continue;
                }
                if (b == complement && count >= 2) {
                    continue;
                }
                
                if (map.containsKey(complement)) {
                    ans.add(List.of(a, complement, b));
                }
                
                map.put(b, count + 1);
            }
        }
        
        return ans;
    }
}