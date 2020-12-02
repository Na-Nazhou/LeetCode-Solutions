class Solution {    
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> combinations = new ArrayList<>();
        combinationSum(candidates, 0, target, combinations, new ArrayList<>());
        return combinations;
    }
    
    private void combinationSum(int[] candidates, int i, int target, List<List<Integer>> combinations, List<Integer> currCombination) {
        if (target == 0) {
            combinations.add(currCombination);
            return;
        }
        
        if (i >= candidates.length || target < 0) {
            return;
        }
        
        List<Integer> copy = new ArrayList<>(currCombination);
        copy.add(candidates[i]);
        combinationSum(candidates, i, target - candidates[i], combinations, copy);
        combinationSum(candidates, i + 1, target, combinations, currCombination);
    }
}
