class Solution {
    public int lengthOfLongestSubstring(String s) {
        int currMax = 0;
        int start = 0;
        
        // { a: 3, b: 1, c: 2}, start = 1, currMax = 3, abc
        // { a: 3, b: 4, c: 2}, start = 2, currMax = 3, bca
        // { a: 3, b: 4, c: 5}, start = 3, currMax = 3, cab
        // { a: 3, b: 6, c: 5}, start = 5, currMax = 3, abc
        // { a: 3, b: 7, c: 5}, start = 7, currMax = 2, bc
        Map<Character, Integer> map = new HashMap<>();
        char[] arr = s.toCharArray();
        for (int i = 0; i < arr.length; i++) {
            char ch = arr[i];
            if (map.containsKey(ch)) {
                int index = map.get(ch);
                if (index >= start) {
                    currMax =  Math.max(currMax, i - start);
                    start = map.get(ch) + 1;
                }
            }
            
            map.put(ch, i);
        }
        
        currMax =  Math.max(currMax, arr.length - start);
        
        return currMax;
    }
}