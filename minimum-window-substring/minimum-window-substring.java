class Solution {
    public String minWindow(String s, String t) {
        if (s.length() == 0 || t.length() == 0) {
            return "";
        }
        
        Map<Character, Integer> target = new HashMap<>();
        for (int i = 0; i < t.length(); i++) {
            char c = t.charAt(i);
            target.put(c, target.getOrDefault(c, 0) + 1);
        }
        int targetCount = target.size();
        
        int minWindowLeft = 0;
        int minWindowRight = s.length() - 1;
        boolean foundAns = false;
        
        int left = 0;
        Map<Character, Integer> count = new HashMap<>();
        int correctCount = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            count.put(c, count.getOrDefault(c, 0) + 1);
            
            if (target.containsKey(c) && count.get(c).equals(target.get(c))) {
                correctCount++;
            }
                
            while (left <= right && correctCount == targetCount) {
                foundAns = true;
                c = s.charAt(left);
                int currWindowLen = right - left + 1;
                if (currWindowLen < minWindowRight - minWindowLeft + 1) {
                    minWindowLeft = left;
                    minWindowRight = right;
                }

                if (target.containsKey(c) && count.get(c).equals(target.get(c))) {
                    correctCount--;
                }
                
                count.put(c, count.get(c) - 1);
                left++;
            }
        }
        
        if (foundAns) {
            return s.substring(minWindowLeft, minWindowRight + 1);
        } else {
            return "";
        }
    }
}