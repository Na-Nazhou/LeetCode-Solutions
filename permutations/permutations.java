class Solution {
    private List<List<Integer>> perms = new ArrayList<>();
    
    public List<List<Integer>> permute(int[] nums) {
        permute(nums, 0);
        return perms;
    }
    
    private void permute(int[] curr, int i) {
        if (i == curr.length) {
            perms.add(Arrays.stream(curr).boxed().collect(Collectors.toList()));
            return;
        }
        
        for (int k = i; k < curr.length; k++) {
            swap(curr, i, k);
            permute(curr, i + 1);
            swap(curr, i, k);
        }    
    }
    
    private void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
