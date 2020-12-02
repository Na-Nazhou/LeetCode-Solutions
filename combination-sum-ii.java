class Solution {   
        public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> combinations = new ArrayList<>();
        combinationSum2(candidates, 0, target, combinations, new ArrayList<>());
        return combinations;
    }
    
    private void combinationSum2(int[] candidates, int i, int target, List<List<Integer>> combinations, List<Integer> currCombination) {
        if (target == 0) {
            combinations.add(currCombination);
            return;
        }
        
        if (i >= candidates.length || target < 0) {
            return;
        }
        
        // Take current number
        List<Integer> copy = new ArrayList<>(currCombination);
        copy.add(candidates[i]);
        combinationSum2(candidates, i + 1, target - candidates[i], combinations, copy);
        
        // Do not take current number
        // Find next unique number
        int next = i+1;
        while (next < candidates.length && candidates[next] == candidates[i]) {
            next++;
        }
        combinationSum2(candidates, next, target, combinations, currCombination);
    }
}
