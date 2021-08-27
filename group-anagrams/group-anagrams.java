class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap();
        for (String s : strs) {
            char[] arr = s.toCharArray();
            Arrays.sort(arr);
            String sorted = String.valueOf(arr);
            map.putIfAbsent(sorted, new ArrayList());
            List<String> group = map.get(sorted);
            group.add(s);
        }
        
        return new ArrayList(map.values());
    }
}