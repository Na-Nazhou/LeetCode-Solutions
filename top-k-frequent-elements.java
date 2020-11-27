class Solution {
    Map<Integer, Integer> freq;
    int[] arr;
    
    public int[] topKFrequent(int[] nums, int k) {
        // O(1) time
        if (k == nums.length) {
            return nums;
        }
        
        freq = new HashMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        
        arr = new int[freq.size()];
        int i = 0;
        for (int num : freq.keySet()) {
            arr[i] = num;
            i++;
        }
        
        // Quick select
        int n = arr.length;
        quickSelect(0, n - 1, n - k);
        
        return Arrays.copyOfRange(arr, n - k, n);
    }
    
    public void quickSelect(int left, int right, int k) {
        if (left == right) {
            return;
        }
        
        Random random = new Random();
        int pivotIdx = left + random.nextInt(right - left + 1);
        pivotIdx = partition(left, right, pivotIdx);
        
        if (pivotIdx == k) {
            return;
        }
        
        if (pivotIdx > k) {
            quickSelect(left, pivotIdx - 1, k);
        } else {
            quickSelect(pivotIdx + 1, right, k);
        }
    }
    
    public int partition(int left, int right, int pivotIdx) {
        int pivot = freq.get(arr[pivotIdx]);
        swap(arr, pivotIdx, right);
        int idx = left;
        for (int i = left; i <= right; i++) {
            if (freq.get(arr[i]) < pivot) {
                swap(arr, idx, i);
                idx++;
            }
        }
        
        swap(arr, idx, right);
        
        return idx;
    }
    
    public void swap(int[] arr, int a, int b) {
        int tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
    }
}
