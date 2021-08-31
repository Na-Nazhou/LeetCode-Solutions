class Solution {
    Map<Integer, Integer> freqMap = new HashMap<>();
    
    public int[] topKFrequent(int[] nums, int k) {
        freqMap = new HashMap<>();
        ArrayList<Integer> arr = new ArrayList<>();
        for (int num : nums) {
            if (!freqMap.containsKey(num)) {
                arr.add(num);
            }
            
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }
        
        nums = new int[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            nums[i] = arr.get(i);
        }
        quickSelect(nums, 0, nums.length - 1, k);
        return Arrays.copyOfRange(nums, 0, k);
    }
    
    private void quickSelect(int[] nums, int left, int right, int k) {
        int pivotIdx = partition(nums, left, right);
        if (pivotIdx > k - 1) {
            quickSelect(nums, left, pivotIdx - 1, k);
        } else if (pivotIdx < k - 1) {
            quickSelect(nums, pivotIdx + 1, right, k);
        }
    }
    
    private int partition(int[] nums, int left, int right) {
        int pivot = freqMap.get(nums[left]);
        int ptr = left; // idx of last num <= pivot
        for (int i = left + 1; i <= right; i++) {
            if (freqMap.get(nums[i]) >= pivot) {
                ptr++;
                swap(nums, ptr, i);
            }
        }
        
        swap(nums, left, ptr);
        return ptr;
        
    }
    
    private void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
        return;
    }
}