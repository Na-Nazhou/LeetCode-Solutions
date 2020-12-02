class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> combinations = new ArrayList<>();
        combinationSum2(1, n, combinations, new ArrayList<>(), k);
        return combinations;   
    }
    
    private void combinationSum2(int i, int target, List<List<Integer>> combinations, List<Integer> currCombination, int k) {
        if (target == 0 && currCombination.size() == k) {
            combinations.add(currCombination);
            return;
        }
        
        if (i >= 10 || target < 0 || currCombination.size() >= k) {
            return;
        }
        
        // Take current number
        List<Integer> copy = new ArrayList<>(currCombination);
        copy.add(i);
        combinationSum2(i + 1, target - i, combinations, copy, k);
        
        // Do not take current number
        combinationSum2(i + 1, target, combinations, currCombination, k);
    }
}
