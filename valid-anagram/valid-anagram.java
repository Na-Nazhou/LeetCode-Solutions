class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> count = new HashMap<>();
        for (char c : s.toCharArray()) {
            count.put(c, count.getOrDefault(c, 0) + 1);
        }
        
        for (char c : t.toCharArray()) {
            if (!count.containsKey(c)) {
                return false;
            }
            
            int freq = count.get(c);
            
            if (freq == 1) {
                count.remove(c);
            } else {
                count.put(c, freq - 1);
            }
        }
        
        return count.isEmpty();
    }
}